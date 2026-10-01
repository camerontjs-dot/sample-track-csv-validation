from __future__ import annotations

import argparse
import hashlib
import json
import secrets
import tempfile
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from sampletrack import SampleTrackDemo, AuthenticationError, AuthorizationError, ValidationError


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@dataclass
class Step:
    name: str
    expected: str
    actual: str
    result: str


@dataclass
class Case:
    test_id: str
    title: str
    steps: list[Step]
    evidence: list[str]
    result: str


class OQRunner:
    def __init__(self, output: Path, tester: str, system_identity: str, execution_id: str):
        self.output = output
        self.tester = tester
        self.system_identity = system_identity
        self.execution_id = execution_id
        self.output.mkdir(parents=True, exist_ok=True)
        self.evidence_dir = self.output / "evidence"
        self.evidence_dir.mkdir(exist_ok=True)
        self.cases: list[Case] = []
        self.counters: dict[str, int] = {}

    def credentials(self) -> dict[str, str]:
        return {
            "WH_OP_01": secrets.token_urlsafe(20),
            "WH_OP_02": secrets.token_urlsafe(20),
            "QA_REVIEW_01": secrets.token_urlsafe(20),
            "SYS_ADMIN_01": secrets.token_urlsafe(20),
            "WH_DISABLED_01": secrets.token_urlsafe(20),
        }

    def fresh(self):
        tmp = tempfile.TemporaryDirectory()
        app = SampleTrackDemo(str(Path(tmp.name) / "sampletrack.sqlite"))
        creds = self.credentials()
        app.bootstrap_fixture_users(creds)
        return app, creds, tmp

    @staticmethod
    def s(name: str, expected: str, actual: str, passed: bool) -> Step:
        return Step(name, expected, actual, "PASS" if passed else "FAIL")

    @staticmethod
    def rejected(func: Callable[[], Any], exc: tuple[type[BaseException], ...]) -> tuple[bool, str]:
        try:
            func()
        except exc as e:
            return True, f"Rejected as expected: {type(e).__name__}: {e}"
        except Exception as e:
            return False, f"Unexpected exception: {type(e).__name__}: {e}"
        return False, "Operation unexpectedly succeeded"

    def evidence(self, tid: str, label: str, payload: Any) -> str:
        n = self.counters.get(tid, 0) + 1
        self.counters[tid] = n
        eid = f"STL-EV-OQ-{tid[-3:]}-{n:02d}"
        path = self.evidence_dir / f"{eid}-{label}.json"
        path.write_text(
            json.dumps(
                {
                    "evidence_id": eid,
                    "execution_id": self.execution_id,
                    "test_id": tid,
                    "captured_at": now_utc(),
                    "system_identity": self.system_identity,
                    "payload": payload,
                },
                indent=2,
                sort_keys=True,
                default=str,
            )
            + "\n",
            encoding="utf-8",
        )
        return eid

    def finish(self, tid: str, title: str, steps: list[Step], evidence: list[str]):
        result = "PASS" if steps and all(x.result == "PASS" for x in steps) and evidence else "FAIL"
        self.cases.append(Case(tid, title, steps, evidence, result))

    def record(self, app, wh, lot="LOT-OQ-001"):
        return app.create_inventory(wh, "DEMO-RX-COLD-001", lot, 24, "REFRIGERATED_2_8C")

    def tc001(self):
        tid, title = "OQ-TC-001", "Valid, invalid, and disabled authentication"
        app, c, tmp = self.fresh(); st=[]; ev=[]
        try:
            ok,a=self.rejected(lambda: app.authenticate("WH_OP_01","wrong"),(AuthenticationError,))
            st.append(self.s("invalid password","Authentication rejected",a,ok))
            try:
                sess=app.authenticate("WH_OP_01",c["WH_OP_01"])
                st.append(self.s("valid password","Warehouse session established",f"{sess.user_id}/{sess.role}",True))
            except Exception as e:
                st.append(self.s("valid password","Warehouse session established",f"{type(e).__name__}: {e}",False))
            ok,a=self.rejected(lambda: app.authenticate("WH_DISABLED_01",c["WH_DISABLED_01"]),(AuthenticationError,))
            st.append(self.s("disabled account","Authentication rejected",a,ok))
            ev.append(self.evidence(tid,"authentication",{"steps":[asdict(x) for x in st]}))
            self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc002(self):
        tid,title="OQ-TC-002","Receiving record identity, required fields, creator/time"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"])
            ok,a=self.rejected(lambda: app.create_inventory(wh,"DEMO-RX-COLD-001","",24,"REFRIGERATED_2_8C"),(ValidationError,))
            st.append(self.s("missing lot","Completion blocked",a,ok))
            r1=self.record(app,wh,"LOT-OQ-001"); row=app.get_record(r1)
            st.append(self.s("complete record","Valid record completes",r1,bool(r1)))
            st.append(self.s("persistent ID","Same ID on retrieval",app.get_record(r1)["record_id"],app.get_record(r1)["record_id"]==r1))
            st.append(self.s("creator/time","WH_OP_01 and creation time recorded",f"{row['received_by']} @ {row['created_at']}",row["received_by"]=="WH_OP_01" and bool(row["created_at"])))
            r2=self.record(app,wh,"LOT-OQ-002")
            st.append(self.s("second identity","Different unique ID",f"{r1} != {r2}",r1!=r2))
            ev.append(self.evidence(tid,"receiving-records",{"record1":row,"record2":app.get_record(r2)}))
            self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc003(self):
        tid,title="OQ-TC-003","Critical manual-data accuracy check"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); qa=app.authenticate("QA_REVIEW_01",c["QA_REVIEW_01"])
            r1=self.record(app,wh)
            ok,a=self.rejected(lambda: app.transition_status(qa,r1,"Released","QA review","QA_REVIEW_01",c["QA_REVIEW_01"]),(ValidationError,))
            st.append(self.s("release before verification","Release blocked",a,ok))
            verified=app.verify_critical_data(qa,r1,"DEMO-RX-COLD-001","LOT-OQ-001","REFRIGERATED_2_8C")
            st.append(self.s("matching verification","Complete and attributable",f"{verified}/{app.get_record(r1)['critical_verified_by']}",verified and app.get_record(r1)["critical_verified_by"]=="QA_REVIEW_01"))
            r2=self.record(app,wh,"LOT-OQ-002")
            bad=app.verify_critical_data(qa,r2,"DEMO-RX-COLD-001","WRONG-LOT","REFRIGERATED_2_8C")
            st.append(self.s("discrepant verification","Does not complete",str(bad),bad is False))
            ok,a=self.rejected(lambda: app.transition_status(qa,r2,"Released","QA review","QA_REVIEW_01",c["QA_REVIEW_01"]),(ValidationError,))
            st.append(self.s("release after mismatch","Release blocked",a,ok))
            ev.append(self.evidence(tid,"critical-verification",{"good":app.get_record(r1),"bad":app.get_record(r2),"bad_audit":app.audit_events(r2)}))
            self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc004(self):
        tid,title="OQ-TC-004","Correction history and deletion prevention"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); qa=app.authenticate("QA_REVIEW_01",c["QA_REVIEW_01"])
            rid=self.record(app,wh)
            app.correct_field(wh,rid,"lot","LOT-OQ-001A","transcription correction")
            corr=[x for x in app.audit_events(rid) if x["action"]=="record_corrected"][-1]
            st.append(self.s("correction history","Prior/new/reason retained",json.dumps(corr,sort_keys=True),corr["old_value"]=="LOT-OQ-001" and corr["new_value"]=="LOT-OQ-001A" and corr["reason"]=="transcription correction"))
            ok,a=self.rejected(lambda: app.attempt_delete_record(wh,rid),(AuthorizationError,))
            st.append(self.s("Warehouse delete","Denied",a,ok))
            ok,a=self.rejected(lambda: app.attempt_delete_record(qa,rid),(AuthorizationError,))
            st.append(self.s("QA delete","Denied",a,ok))
            st.append(self.s("record retained","Corrected record retrievable",app.get_record(rid)["lot"],app.get_record(rid)["lot"]=="LOT-OQ-001A"))
            ev.append(self.evidence(tid,"correction-history",{"record":app.get_record(rid),"audit":app.audit_events(rid)}))
            self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc005(self):
        tid,title="OQ-TC-005","Record retrieval, related history, and record copies"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); rid=self.record(app,wh); app.assign_location(wh,rid,"REFR-A1")
            byid=app.get_record(rid); bylot=app.find_by_lot("LOT-OQ-001"); electronic=app.export_electronic(rid); human=app.export_human_readable(rid)
            st.append(self.s("retrieve by ID","Correct record",byid["record_id"],byid["record_id"]==rid))
            st.append(self.s("retrieve by lot","Same record unambiguous",str([x["record_id"] for x in bylot]),len(bylot)==1 and bylot[0]["record_id"]==rid))
            st.append(self.s("related history","History linked",f"custody={len(electronic['custody'])};audit={len(electronic['audit'])}",len(electronic["custody"])>=1 and len(electronic["audit"])>=1))
            st.append(self.s("electronic copy","Accurate structured copy",str(sorted(electronic.keys())),electronic["record"]["record_id"]==rid and set(electronic)=={"record","custody","excursions","audit","signatures"}))
            human_ok=rid in human and "LOT-OQ-001" in human and "Custody history:" in human and "Audit trail:" in human and "Signatures:" in human
            st.append(self.s("human-readable copy","Readable record/history copy",human[:180].replace("\n"," | "),human_ok))
            ev.append(self.evidence(tid,"electronic-copy",electronic)); ev.append(self.evidence(tid,"human-readable-copy",{"text":human}))
            self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc006(self):
        tid,title="OQ-TC-006","Storage condition/location compatibility"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); rid=self.record(app,wh)
            st.append(self.s("required condition","REFRIGERATED_2_8C",app.get_record(rid)["storage_condition"],app.get_record(rid)["storage_condition"]=="REFRIGERATED_2_8C"))
            app.assign_location(wh,rid,"REFR-A1"); st.append(self.s("compatible","REFR-A1 accepted",app.get_record(rid)["location"],app.get_record(rid)["location"]=="REFR-A1"))
            ok,a=self.rejected(lambda: app.assign_location(wh,rid,"CRT-A1"),(ValidationError,)); st.append(self.s("incompatible","CRT-A1 rejected",a,ok))
            ok,a=self.rejected(lambda: app.assign_location(wh,rid,"RETIRED-R1"),(ValidationError,)); st.append(self.s("inactive","RETIRED-R1 rejected",a,ok))
            app.assign_location(wh,rid,"REFR-A2")
            st.append(self.s("second compatible","REFR-A2 accepted with retained history",f"{app.get_record(rid)['location']}/{len(app.custody_events(rid))}",app.get_record(rid)["location"]=="REFR-A2" and len(app.custody_events(rid))==2))
            ev.append(self.evidence(tid,"location-history",{"record":app.get_record(rid),"custody":app.custody_events(rid),"audit":app.audit_events(rid)}))
            self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc007(self):
        tid,title="OQ-TC-007","Initial and controlled material statuses"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); rid=self.record(app,wh)
            st.append(self.s("initial status","Quarantine",app.get_record(rid)["status"],app.get_record(rid)["status"]=="Quarantine"))
            expected={"Quarantine","Released","On Hold","Rejected","Returned","Recalled"}; actual=set(app.list_statuses())
            st.append(self.s("controlled values","Six configured values present",str(sorted(actual)),expected.issubset(actual)))
            ok,a=self.rejected(lambda: app.transition_status(wh,rid,"AVAILABLE-NOW"),(ValidationError,)); st.append(self.s("free-text status","Rejected",a,ok))
            st.append(self.s("valid state retained","Quarantine",app.get_record(rid)["status"],app.get_record(rid)["status"]=="Quarantine"))
            ev.append(self.evidence(tid,"status-control",{"record":app.get_record(rid),"statuses":list(app.list_statuses())}))
            self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc008(self):
        tid,title="OQ-TC-008","Status sequencing, QA authority, and rationale"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); qa=app.authenticate("QA_REVIEW_01",c["QA_REVIEW_01"]); rid=self.record(app,wh)
            app.verify_critical_data(qa,rid,"DEMO-RX-COLD-001","LOT-OQ-001","REFRIGERATED_2_8C")
            ok,a=self.rejected(lambda: app.transition_status(wh,rid,"Released","release","WH_OP_01",c["WH_OP_01"]),(AuthorizationError,)); st.append(self.s("Warehouse release","Denied",a,ok))
            ok,a=self.rejected(lambda: app.transition_status(qa,rid,"Released",None,"QA_REVIEW_01",c["QA_REVIEW_01"]),(ValidationError,)); st.append(self.s("QA release without rationale","Denied",a,ok))
            app.transition_status(qa,rid,"Released","QA review complete","QA_REVIEW_01",c["QA_REVIEW_01"])
            st.append(self.s("QA release","Released",app.get_record(rid)["status"],app.get_record(rid)["status"]=="Released"))
            last=[x for x in app.audit_events(rid) if x["action"]=="status_changed"][-1]
            st.append(self.s("status history","Prior/new/user/time/rationale retained",json.dumps(last,sort_keys=True),last["old_value"]=="Quarantine" and last["new_value"]=="Released" and last["actor"]=="QA_REVIEW_01" and last["reason"]=="QA review complete"))
            ok,a=self.rejected(lambda: app.transition_status(qa,rid,"Rejected","bypass","QA_REVIEW_01",c["QA_REVIEW_01"]),(ValidationError,)); st.append(self.s("prohibited sequence","Rejected",a,ok))
            ev.append(self.evidence(tid,"status-authority",{"record":app.get_record(rid),"audit":app.audit_events(rid),"signatures":app.signature_events(rid)}))
            self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc009(self):
        tid,title="OQ-TC-009","Temperature lower/upper boundary behavior"
        oracle=[(1.9,"Excursion"),(2.0,"Within range"),(2.1,"Within range"),(7.9,"Within range"),(8.0,"Within range"),(8.1,"Excursion")]
        st=[]; ev=[]; payload=[]
        for value,expected in oracle:
            app,c,tmp=self.fresh()
            try:
                wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); rid=self.record(app,wh,f"LOT-T-{value}")
                result=app.record_temperature(wh,rid,value,"2026-09-30T12:00:00+00:00","mock logger","10 min")
                actual=result["classification"]; st.append(self.s(f"{value:.1f} C",expected,actual,actual==expected))
                payload.append({"temperature":value,"expected":expected,"actual":actual,"record":app.get_record(rid),"excursions":app.excursion_events(rid)})
            finally:
                app.close(); tmp.cleanup()
        ev.append(self.evidence(tid,"temperature-boundaries",payload)); self.finish(tid,title,st,ev)

    def tc010(self):
        tid,title="OQ-TC-010","Excursion-record completeness and linkage"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); rid=self.record(app,wh)
            ok,a=self.rejected(lambda: app.record_temperature(wh,rid,8.1,"2026-09-30T12:00:00+00:00","", "10 min"),(ValidationError,)); st.append(self.s("missing source","Rejected",a,ok))
            result=app.record_temperature(wh,rid,8.1,"2026-09-30T12:00:00+00:00","mock logger","10 min"); e=app.excursion_events(rid)[-1]
            st.append(self.s("complete excursion","Saved",f"{result['classification']}/{result['excursion_id']}",result["classification"]=="Excursion" and result["excursion_id"] is not None))
            ok=e["record_id"]==rid and e["temperature"]==8.1 and e["source"]=="mock logger" and e["reporter"]=="WH_OP_01"
            st.append(self.s("record linkage/content","Correct record/temp/source/reporter",json.dumps(e,sort_keys=True),ok))
            ev.append(self.evidence(tid,"excursion-record",{"record":app.get_record(rid),"excursions":app.excursion_events(rid)})); self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc011(self):
        tid,title="OQ-TC-011","Excursion hold enforcement and QA disposition"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); qa=app.authenticate("QA_REVIEW_01",c["QA_REVIEW_01"]); rid=self.record(app,wh)
            app.verify_critical_data(qa,rid,"DEMO-RX-COLD-001","LOT-OQ-001","REFRIGERATED_2_8C"); app.transition_status(qa,rid,"Released","initial QA release","QA_REVIEW_01",c["QA_REVIEW_01"])
            app.record_temperature(wh,rid,8.1,"2026-09-30T12:00:00+00:00","mock logger","10 min")
            st.append(self.s("excursion hold","On Hold",app.get_record(rid)["status"],app.get_record(rid)["status"]=="On Hold"))
            ok,a=self.rejected(lambda: app.transition_status(wh,rid,"Released","warehouse attempt","WH_OP_01",c["WH_OP_01"]),(AuthorizationError,)); st.append(self.s("Warehouse release","Denied",a,ok))
            ok,a=self.rejected(lambda: app.disposition_excursion(qa,rid,"Released","","QA_REVIEW_01",c["QA_REVIEW_01"]),(ValidationError,)); st.append(self.s("QA no rationale","Denied",a,ok))
            sig=app.disposition_excursion(qa,rid,"Released","mock technical disposition: acceptable for workflow test","QA_REVIEW_01",c["QA_REVIEW_01"]); e=app.excursion_events(rid)[-1]
            st.append(self.s("QA disposition","Released with rationale/signature",f"{app.get_record(rid)['status']}/sig={sig}",app.get_record(rid)["status"]=="Released" and bool(e["rationale"]) and e["signature_id"]==sig))
            ev.append(self.evidence(tid,"excursion-disposition",{"record":app.get_record(rid),"excursions":app.excursion_events(rid),"audit":app.audit_events(rid),"signatures":app.signature_events(rid)})); self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc012(self):
        tid,title="OQ-TC-012","Chain-of-custody history"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            w1=app.authenticate("WH_OP_01",c["WH_OP_01"]); w2=app.authenticate("WH_OP_02",c["WH_OP_02"]); rid=self.record(app,w1)
            app.assign_location(w1,rid,"REFR-A1"); app.custody_transfer(w2,rid,"REFR-A2"); e=app.custody_events(rid)
            st.append(self.s("first event","WH_OP_01 to REFR-A1",json.dumps(e[0],sort_keys=True),len(e)>=1 and e[0]["actor"]=="WH_OP_01" and e[0]["to_location"]=="REFR-A1"))
            st.append(self.s("second event","WH_OP_02 REFR-A1 to REFR-A2",json.dumps(e[1],sort_keys=True),len(e)==2 and e[1]["actor"]=="WH_OP_02" and e[1]["from_location"]=="REFR-A1" and e[1]["to_location"]=="REFR-A2"))
            st.append(self.s("history retained","Two events/current REFR-A2",f"{len(e)}/{app.get_record(rid)['location']}",len(e)==2 and app.get_record(rid)["location"]=="REFR-A2"))
            ev.append(self.evidence(tid,"custody-history",{"record":app.get_record(rid),"custody":e})); self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc013(self):
        tid,title="OQ-TC-013","Unique identity and role-based authorization"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            ad=app.authenticate("SYS_ADMIN_01",c["SYS_ADMIN_01"]); wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); qa=app.authenticate("QA_REVIEW_01",c["QA_REVIEW_01"])
            ok,a=self.rejected(lambda: app.create_user(ad,"WH_OP_01","Duplicate","Warehouse Operator",secrets.token_urlsafe(12)),(ValidationError,)); st.append(self.s("duplicate identity","Rejected",a,ok))
            rid=self.record(app,wh)
            ok,a=self.rejected(lambda: app.transition_status(wh,rid,"Released","unauthorized","WH_OP_01",c["WH_OP_01"]),(AuthorizationError,)); st.append(self.s("Warehouse QA action","Denied",a,ok))
            ok,a=self.rejected(lambda: app.create_user(wh,"TEMP1","Temp","Warehouse Operator","x"),(AuthorizationError,)); st.append(self.s("Warehouse admin","Denied",a,ok))
            ok,a=self.rejected(lambda: app.create_user(qa,"TEMP2","Temp","Warehouse Operator","x"),(AuthorizationError,)); st.append(self.s("QA admin","Denied",a,ok))
            ok,a=self.rejected(lambda: app.transition_status(ad,rid,"Released","admin attempt","SYS_ADMIN_01",c["SYS_ADMIN_01"]),(AuthorizationError,)); st.append(self.s("Admin QA action","Denied",a,ok))
            ev.append(self.evidence(tid,"rbac",{"steps":[asdict(x) for x in st],"record":app.get_record(rid)})); self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc014(self):
        tid,title="OQ-TC-014","Access-authorisation lifecycle record"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            ad=app.authenticate("SYS_ADMIN_01",c["SYS_ADMIN_01"]); pw=secrets.token_urlsafe(20)
            app.create_user(ad,"TEMP_ACCESS_01","Mock Temporary User","Warehouse Operator",pw); app.change_user_role(ad,"TEMP_ACCESS_01","QA Reviewer"); app.disable_user(ad,"TEMP_ACCESS_01")
            events=app.access_events("TEMP_ACCESS_01"); actions=[x["action"] for x in events]
            st.append(self.s("lifecycle history","created, role_changed, disabled",str(actions),actions==["created","role_changed","disabled"]))
            st.append(self.s("admin attribution","Admin and time on every event",json.dumps(events,sort_keys=True),all(x["actor"]=="SYS_ADMIN_01" and x["at"] for x in events)))
            ok,a=self.rejected(lambda: app.authenticate("TEMP_ACCESS_01",pw),(AuthenticationError,)); st.append(self.s("disabled login","Rejected",a,ok))
            ev.append(self.evidence(tid,"access-lifecycle",{"events":events})); self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc015(self):
        tid,title="OQ-TC-015","Audit-trail coverage, content, immutability, reviewability"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); qa=app.authenticate("QA_REVIEW_01",c["QA_REVIEW_01"]); rid=self.record(app,wh)
            app.correct_field(wh,rid,"lot","LOT-OQ-001A","transcription correction"); app.verify_critical_data(qa,rid,"DEMO-RX-COLD-001","LOT-OQ-001A","REFRIGERATED_2_8C")
            app.transition_status(qa,rid,"Released","QA release","QA_REVIEW_01",c["QA_REVIEW_01"]); app.record_temperature(wh,rid,8.1,"2026-09-30T12:00:00+00:00","mock logger","10 min"); app.disposition_excursion(qa,rid,"Rejected","mock technical disposition","QA_REVIEW_01",c["QA_REVIEW_01"])
            audit=app.audit_events(rid); actions={x["action"] for x in audit}; needed={"record_created","record_corrected","status_changed","excursion_created","electronic_signature","excursion_disposition"}
            st.append(self.s("event coverage","Representative GMP events present",str(sorted(actions)),needed.issubset(actions)))
            corr=[x for x in audit if x["action"]=="record_corrected"][-1]; ok=corr["actor"]=="WH_OP_01" and corr["at"] and corr["old_value"]=="LOT-OQ-001" and corr["new_value"]=="LOT-OQ-001A" and corr["reason"]=="transcription correction"
            st.append(self.s("change content","User/time/prior/new/reason",json.dumps(corr,sort_keys=True),ok))
            ok,a=self.rejected(lambda: app.attempt_modify_audit(wh,audit[0]["id"]),(AuthorizationError,)); st.append(self.s("audit modification","Denied",a,ok))
            st.append(self.s("QA reviewability","Chronological intelligible trail",f"{len(audit)} events",len(audit)>=6 and all(x["at"] and x["actor"] and x["action"] for x in audit)))
            ev.append(self.evidence(tid,"audit-trail",{"record":app.get_record(rid),"audit":audit,"signatures":app.signature_events(rid),"excursions":app.excursion_events(rid)})); self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc016(self):
        tid,title="OQ-TC-016","Electronic-signature manifestation and record linkage"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); qa=app.authenticate("QA_REVIEW_01",c["QA_REVIEW_01"]); rid=self.record(app,wh)
            app.verify_critical_data(qa,rid,"DEMO-RX-COLD-001","LOT-OQ-001","REFRIGERATED_2_8C"); sigid=app.transition_status(qa,rid,"Released","QA release","QA_REVIEW_01",c["QA_REVIEW_01"]); sig=app.signature_events(rid)[-1]
            st.append(self.s("signature completion","Linked to signed record",f"{sigid}/{sig['record_id']}",sigid is not None and sig["record_id"]==rid))
            st.append(self.s("manifestation","Name/time/meaning present",json.dumps(sig,sort_keys=True),sig["display_name"]=="Mock QA Reviewer 01" and bool(sig["signed_at"]) and "Released" in sig["meaning"]))
            st.append(self.s("persistent linkage","Same signature after retrieval",str([x["id"] for x in app.signature_events(rid)]),any(x["id"]==sigid and x["record_id"]==rid for x in app.signature_events(rid))))
            human=app.export_human_readable(rid); st.append(self.s("human-readable signature","Signature included",human[-240:].replace("\n"," | "),"Mock QA Reviewer 01" in human and "Released disposition" in human))
            rid2=self.record(app,wh,"LOT-OQ-002"); ok,a=self.rejected(lambda: app.attempt_transfer_signature(qa,sigid,rid2),(AuthorizationError,)); st.append(self.s("signature transfer","Denied/no target signature",a,ok and len(app.signature_events(rid2))==0))
            ev.append(self.evidence(tid,"signature-linkage",{"record":app.get_record(rid),"signatures":app.signature_events(rid),"human_readable":human})); self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc017(self):
        tid,title="OQ-TC-017","Electronic-signature identity and credential challenge"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); qa=app.authenticate("QA_REVIEW_01",c["QA_REVIEW_01"]); rid=self.record(app,wh)
            app.verify_critical_data(qa,rid,"DEMO-RX-COLD-001","LOT-OQ-001","REFRIGERATED_2_8C")
            ok,a=self.rejected(lambda: app.transition_status(qa,rid,"Released","QA release","QA_REVIEW_01","wrong-password"),(AuthenticationError,)); st.append(self.s("wrong password","Rejected/no disposition",a,ok and app.get_record(rid)["status"]=="Quarantine"))
            ok,a=self.rejected(lambda: app.transition_status(qa,rid,"Released","QA release","WH_OP_01",c["QA_REVIEW_01"]),(AuthenticationError,)); st.append(self.s("different ID code","Rejected/no disposition",a,ok and app.get_record(rid)["status"]=="Quarantine"))
            ok,a=self.rejected(lambda: app.transition_status(wh,rid,"Released","Warehouse attempt","WH_OP_01",c["WH_OP_01"]),(AuthorizationError,)); st.append(self.s("Warehouse signed action","Denied",a,ok))
            app.transition_status(qa,rid,"Released","QA release","QA_REVIEW_01",c["QA_REVIEW_01"]); sig=app.signature_events(rid)[-1]
            st.append(self.s("correct QA credentials","Succeeds/attributed",f"{app.get_record(rid)['status']}/{sig['actor']}",app.get_record(rid)["status"]=="Released" and sig["actor"]=="QA_REVIEW_01"))
            ev.append(self.evidence(tid,"signature-authentication",{"record":app.get_record(rid),"signatures":app.signature_events(rid),"audit":app.audit_events(rid)})); self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def tc018(self):
        tid,title="OQ-TC-018","End-to-end regulated workflow"
        app,c,tmp=self.fresh(); st=[]; ev=[]
        try:
            wh=app.authenticate("WH_OP_01",c["WH_OP_01"]); qa=app.authenticate("QA_REVIEW_01",c["QA_REVIEW_01"]); rid=self.record(app,wh,"LOT-OQ-004")
            st.append(self.s("receive","Unique Quarantine record",f"{rid}/{app.get_record(rid)['status']}",bool(rid) and app.get_record(rid)["status"]=="Quarantine" and app.get_record(rid)["received_by"]=="WH_OP_01"))
            verified=app.verify_critical_data(qa,rid,"DEMO-RX-COLD-001","LOT-OQ-004","REFRIGERATED_2_8C"); st.append(self.s("critical verification","Attributable QA verification",f"{verified}/{app.get_record(rid)['critical_verified_by']}",verified and app.get_record(rid)["critical_verified_by"]=="QA_REVIEW_01"))
            app.assign_location(wh,rid,"REFR-A1"); app.transition_status(qa,rid,"Released","initial QA release","QA_REVIEW_01",c["QA_REVIEW_01"]); st.append(self.s("location/release","Compatible location and signed release",f"{app.get_record(rid)['location']}/{app.get_record(rid)['status']}",app.get_record(rid)["location"]=="REFR-A1" and app.get_record(rid)["status"]=="Released"))
            app.custody_transfer(wh,rid,"REFR-A2"); st.append(self.s("custody transfer","Second event appended",str(len(app.custody_events(rid))),len(app.custody_events(rid))==2))
            result=app.record_temperature(wh,rid,8.1,"2026-09-30T12:00:00+00:00","mock logger","10 min"); st.append(self.s("8.1 C excursion","Excursion and On Hold",f"{result['classification']}/{app.get_record(rid)['status']}",result["classification"]=="Excursion" and app.get_record(rid)["status"]=="On Hold"))
            ok,a=self.rejected(lambda: app.transition_status(wh,rid,"Released","Warehouse attempt","WH_OP_01",c["WH_OP_01"]),(AuthorizationError,)); st.append(self.s("Warehouse re-release","Denied",a,ok))
            app.disposition_excursion(qa,rid,"Released","mock technical disposition: acceptable for workflow test","QA_REVIEW_01",c["QA_REVIEW_01"]); st.append(self.s("QA excursion disposition","Signed release",app.get_record(rid)["status"],app.get_record(rid)["status"]=="Released"))
            electronic=app.export_electronic(rid); human=app.export_human_readable(rid)
            linked=bool(electronic["custody"]) and bool(electronic["excursions"]) and bool(electronic["audit"]) and len(electronic["signatures"])>=2
            st.append(self.s("linked final history","All history linked",f"custody={len(electronic['custody'])};excursions={len(electronic['excursions'])};audit={len(electronic['audit'])};signatures={len(electronic['signatures'])}",linked))
            st.append(self.s("human-readable output","Record and signatures present",human[:220].replace("\n"," | "),rid in human and "LOT-OQ-004" in human and "Mock QA Reviewer 01" in human))
            actions=[x["action"] for x in electronic["audit"]]; st.append(self.s("sequence reconstruction","Creation/excursion/disposition reconstructable",str(actions),"record_created" in actions and "excursion_created" in actions and "excursion_disposition" in actions))
            ev.append(self.evidence(tid,"end-to-end-record",{"electronic":electronic,"human_readable":human})); self.finish(tid,title,st,ev)
        finally:
            app.close(); tmp.cleanup()

    def run(self) -> int:
        for n in range(1,19):
            getattr(self,f"tc{n:03d}")()
        self.write_outputs()
        return 0 if all(x.result=="PASS" for x in self.cases) else 1

    def write_outputs(self):
        doc={
            "execution_id":self.execution_id,
            "executed_at":now_utc(),
            "tester":self.tester,
            "system_identity":self.system_identity,
            "protocol":"STL-OQ-001",
            "summary":{"total":len(self.cases),"pass":sum(x.result=="PASS" for x in self.cases),"fail":sum(x.result=="FAIL" for x in self.cases)},
            "results":[asdict(x) for x in self.cases],
        }
        (self.output/"execution.json").write_text(json.dumps(doc,indent=2,sort_keys=True)+"\n",encoding="utf-8")
        lines=[
            "# STL-OQ-001 Execution Record","",
            "> MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE","",
            f"- Execution ID: {self.output.name}",
            f"- Tester: {self.tester}",
            f"- System identity: {self.system_identity}",
            f"- Executed at: {doc['executed_at']}",
            f"- Result: {doc['summary']['pass']} PASS / {doc['summary']['fail']} FAIL","",
        ]
        for case in self.cases:
            lines += [f"## {case.test_id} — {case.title}","",f"Result: {case.result}","","| Step | Expected | Actual | Result |","|---|---|---|---|"]
            for x in case.steps:
                clean=lambda z:str(z).replace("|","\\|").replace("\n","<br>")
                lines.append(f"| {clean(x.name)} | {clean(x.expected)} | {clean(x.actual)} | {x.result} |")
            lines += ["",f"Evidence: {', '.join(case.evidence) if case.evidence else 'NONE'}",""]
        (self.output/"execution.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
        manifest=[]
        for path in sorted(self.output.rglob("*")):
            if path.is_file() and path.name!="manifest.json":
                manifest.append({"path":str(path.relative_to(self.output)),"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
        (self.output/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")


def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True)
    p.add_argument("--tester",required=True)
    p.add_argument("--system-identity",required=True)
    p.add_argument("--execution-id",required=True)
    a=p.parse_args()
    return OQRunner(Path(a.output),a.tester,a.system_identity,a.execution_id).run()


if __name__=="__main__":
    raise SystemExit(main())
