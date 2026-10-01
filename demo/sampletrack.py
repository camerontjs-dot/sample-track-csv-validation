from __future__ import annotations

import hashlib
import sqlite3
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


class SampleTrackError(Exception):
    pass


class AuthenticationError(SampleTrackError):
    pass


class AuthorizationError(SampleTrackError):
    pass


class ValidationError(SampleTrackError):
    pass


class NotFoundError(SampleTrackError):
    pass


@dataclass(frozen=True)
class Session:
    user_id: str
    role: str


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def password_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class SampleTrackDemo:
    """Custom demonstration surrogate for the fictional SampleTrack Lite scenario.

    This is not the fictional GAMP Category 4 supplier product.
    """

    VALID_STATUSES = ("Quarantine", "Released", "On Hold", "Rejected", "Returned", "Recalled")
    ROLES = ("Warehouse Operator", "QA Reviewer", "System Administrator")

    def __init__(self, db_path: str = ":memory:") -> None:
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._create_schema()
        self._seed_configuration()

    def close(self) -> None:
        self.conn.close()

    def _create_schema(self) -> None:
        self.conn.executescript(
            """
            PRAGMA foreign_keys = ON;

            CREATE TABLE users (
                user_id TEXT PRIMARY KEY,
                display_name TEXT NOT NULL,
                role TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                active INTEGER NOT NULL CHECK(active IN (0,1))
            );

            CREATE TABLE access_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_user TEXT NOT NULL,
                actor TEXT NOT NULL,
                at TEXT NOT NULL,
                action TEXT NOT NULL,
                old_role TEXT,
                new_role TEXT
            );

            CREATE TABLE products (
                product_id TEXT PRIMARY KEY,
                description TEXT NOT NULL,
                storage_condition TEXT NOT NULL,
                lower_limit REAL NOT NULL,
                upper_limit REAL NOT NULL
            );

            CREATE TABLE locations (
                location_id TEXT PRIMARY KEY,
                storage_condition TEXT NOT NULL,
                active INTEGER NOT NULL CHECK(active IN (0,1))
            );

            CREATE TABLE inventory (
                record_id TEXT PRIMARY KEY,
                product_id TEXT NOT NULL,
                lot TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                storage_condition TEXT NOT NULL,
                received_by TEXT NOT NULL,
                created_at TEXT NOT NULL,
                status TEXT NOT NULL,
                location TEXT,
                critical_verified_by TEXT,
                critical_verified_at TEXT
            );

            CREATE TABLE custody (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                record_id TEXT NOT NULL,
                actor TEXT NOT NULL,
                at TEXT NOT NULL,
                from_location TEXT,
                to_location TEXT NOT NULL
            );

            CREATE TABLE excursions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                record_id TEXT NOT NULL,
                temperature REAL NOT NULL,
                event_at TEXT NOT NULL,
                reporter TEXT NOT NULL,
                source TEXT NOT NULL,
                duration_details TEXT,
                classification TEXT NOT NULL,
                disposition TEXT,
                rationale TEXT,
                disposition_by TEXT,
                disposition_at TEXT,
                signature_id INTEGER
            );

            CREATE TABLE signatures (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                record_id TEXT NOT NULL,
                actor TEXT NOT NULL,
                display_name TEXT NOT NULL,
                signed_at TEXT NOT NULL,
                meaning TEXT NOT NULL,
                action_ref TEXT NOT NULL
            );

            CREATE TABLE audit (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                record_id TEXT,
                actor TEXT NOT NULL,
                at TEXT NOT NULL,
                action TEXT NOT NULL,
                field TEXT,
                old_value TEXT,
                new_value TEXT,
                reason TEXT
            );
            """
        )
        self.conn.commit()

    def _seed_configuration(self) -> None:
        self.conn.executemany(
            "INSERT INTO products VALUES (?,?,?,?,?)",
            [
                ("DEMO-RX-COLD-001", "Fictional refrigerated demonstration product", "REFRIGERATED_2_8C", 2.0, 8.0),
                ("DEMO-RX-ROOM-001", "Fictional room-temperature demonstration product", "CONTROLLED_ROOM_15_25C", 15.0, 25.0),
            ],
        )
        self.conn.executemany(
            "INSERT INTO locations VALUES (?,?,?)",
            [
                ("REFR-A1", "REFRIGERATED_2_8C", 1),
                ("REFR-A2", "REFRIGERATED_2_8C", 1),
                ("CRT-A1", "CONTROLLED_ROOM_15_25C", 1),
                ("RETIRED-R1", "REFRIGERATED_2_8C", 0),
            ],
        )
        self.conn.commit()

    def bootstrap_fixture_users(self, credentials: dict[str, str]) -> None:
        rows = [
            ("WH_OP_01", "Mock Warehouse Operator 01", "Warehouse Operator", 1),
            ("WH_OP_02", "Mock Warehouse Operator 02", "Warehouse Operator", 1),
            ("QA_REVIEW_01", "Mock QA Reviewer 01", "QA Reviewer", 1),
            ("SYS_ADMIN_01", "Mock System Administrator 01", "System Administrator", 1),
            ("WH_DISABLED_01", "Mock Disabled Warehouse Operator", "Warehouse Operator", 0),
        ]
        self.conn.executemany(
            "INSERT INTO users VALUES (?,?,?,?,?)",
            [(uid, name, role, password_hash(credentials[uid]), active) for uid, name, role, active in rows],
        )
        self.conn.commit()

    def authenticate(self, user_id: str, password: str) -> Session:
        row = self.conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
        if row is None or not row["active"] or row["password_hash"] != password_hash(password):
            raise AuthenticationError("authentication failed")
        return Session(row["user_id"], row["role"])

    def _require_role(self, session: Session, *roles: str) -> None:
        if session.role not in roles:
            raise AuthorizationError(f"{session.role} not authorized")

    def _record(self, record_id: str) -> sqlite3.Row:
        row = self.conn.execute("SELECT * FROM inventory WHERE record_id=?", (record_id,)).fetchone()
        if row is None:
            raise NotFoundError(record_id)
        return row

    def _audit(
        self,
        actor: str,
        action: str,
        record_id: str | None = None,
        field: str | None = None,
        old_value: Any = None,
        new_value: Any = None,
        reason: str | None = None,
    ) -> None:
        self.conn.execute(
            "INSERT INTO audit(record_id,actor,at,action,field,old_value,new_value,reason) VALUES (?,?,?,?,?,?,?,?)",
            (
                record_id, actor, utc_now(), action, field,
                None if old_value is None else str(old_value),
                None if new_value is None else str(new_value),
                reason,
            ),
        )

    def create_inventory(self, session: Session, product_id: str, lot: str, quantity: int, storage_condition: str) -> str:
        self._require_role(session, "Warehouse Operator", "QA Reviewer")
        if not product_id or not lot or quantity is None or not storage_condition:
            raise ValidationError("required receiving fields missing")
        product = self.conn.execute("SELECT * FROM products WHERE product_id=?", (product_id,)).fetchone()
        if product is None:
            raise ValidationError("unknown product")
        if storage_condition != product["storage_condition"]:
            raise ValidationError("storage condition does not match configured product")
        record_id = f"STL-{uuid.uuid4().hex[:12].upper()}"
        created = utc_now()
        self.conn.execute(
            "INSERT INTO inventory VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (record_id, product_id, lot, int(quantity), storage_condition, session.user_id, created, "Quarantine", None, None, None),
        )
        self._audit(session.user_id, "record_created", record_id, new_value="Quarantine")
        self.conn.commit()
        return record_id

    def correct_field(self, session: Session, record_id: str, field: str, new_value: str, reason: str) -> None:
        self._require_role(session, "Warehouse Operator", "QA Reviewer")
        if field not in {"lot", "quantity"} or not reason:
            raise ValidationError("invalid correction")
        row = self._record(record_id)
        old = row[field]
        self.conn.execute(f"UPDATE inventory SET {field}=? WHERE record_id=?", (new_value, record_id))
        self._audit(session.user_id, "record_corrected", record_id, field, old, new_value, reason)
        self.conn.commit()

    def attempt_delete_record(self, session: Session, record_id: str) -> None:
        self._record(record_id)
        self._require_role(session, "Warehouse Operator", "QA Reviewer")
        raise AuthorizationError("permanent deletion of completed GxP record is not permitted")

    def verify_critical_data(self, session: Session, record_id: str, product_id: str, lot: str, storage_condition: str) -> bool:
        self._require_role(session, "QA Reviewer")
        row = self._record(record_id)
        matches = row["product_id"] == product_id and row["lot"] == lot and row["storage_condition"] == storage_condition
        if not matches:
            self._audit(session.user_id, "critical_verification_failed", record_id, reason="critical data mismatch")
            self.conn.commit()
            return False
        at = utc_now()
        self.conn.execute(
            "UPDATE inventory SET critical_verified_by=?, critical_verified_at=? WHERE record_id=?",
            (session.user_id, at, record_id),
        )
        self._audit(session.user_id, "critical_verification_complete", record_id)
        self.conn.commit()
        return True

    def assign_location(self, session: Session, record_id: str, location_id: str) -> None:
        self._require_role(session, "Warehouse Operator", "QA Reviewer")
        row = self._record(record_id)
        loc = self.conn.execute("SELECT * FROM locations WHERE location_id=?", (location_id,)).fetchone()
        if loc is None or not loc["active"]:
            raise ValidationError("location is inactive or unknown")
        if loc["storage_condition"] != row["storage_condition"]:
            raise ValidationError("location incompatible with required storage condition")
        old = row["location"]
        self.conn.execute("UPDATE inventory SET location=? WHERE record_id=?", (location_id, record_id))
        self.conn.execute(
            "INSERT INTO custody(record_id,actor,at,from_location,to_location) VALUES (?,?,?,?,?)",
            (record_id, session.user_id, utc_now(), old, location_id),
        )
        self._audit(session.user_id, "location_changed", record_id, "location", old, location_id)
        self.conn.commit()

    def custody_transfer(self, session: Session, record_id: str, to_location: str) -> None:
        self.assign_location(session, record_id, to_location)

    def list_statuses(self) -> tuple[str, ...]:
        return self.VALID_STATUSES

    def _verify_signature_credentials(self, session: Session, signing_user_id: str, password: str) -> None:
        if session.user_id != signing_user_id:
            raise AuthenticationError("signature identity does not match authenticated user")
        row = self.conn.execute("SELECT * FROM users WHERE user_id=?", (signing_user_id,)).fetchone()
        if row is None or not row["active"] or row["password_hash"] != password_hash(password):
            raise AuthenticationError("signature authentication failed")

    def _signature(self, session: Session, record_id: str, meaning: str, action_ref: str, signing_user_id: str, password: str) -> int:
        self._require_role(session, "QA Reviewer")
        self._verify_signature_credentials(session, signing_user_id, password)
        user = self.conn.execute("SELECT display_name FROM users WHERE user_id=?", (session.user_id,)).fetchone()
        cur = self.conn.execute(
            "INSERT INTO signatures(record_id,actor,display_name,signed_at,meaning,action_ref) VALUES (?,?,?,?,?,?)",
            (record_id, session.user_id, user["display_name"], utc_now(), meaning, action_ref),
        )
        sig_id = int(cur.lastrowid)
        self._audit(session.user_id, "electronic_signature", record_id, new_value=f"signature:{sig_id}", reason=meaning)
        return sig_id

    def transition_status(
        self,
        session: Session,
        record_id: str,
        new_status: str,
        reason: str | None = None,
        signing_user_id: str | None = None,
        password: str | None = None,
    ) -> int | None:
        row = self._record(record_id)
        if new_status not in self.VALID_STATUSES:
            raise ValidationError("unconfigured status")
        old = row["status"]
        if old == new_status:
            return None
        allowed = {
            ("Quarantine", "Released"), ("Quarantine", "On Hold"), ("Quarantine", "Rejected"),
            ("Released", "On Hold"), ("On Hold", "Released"), ("On Hold", "Rejected"),
            ("Released", "Recalled"),
        }
        if (old, new_status) not in allowed:
            raise ValidationError("prohibited status transition")
        sig_id = None
        qa_required = new_status in {"Released", "Rejected", "Recalled"}
        if qa_required:
            self._require_role(session, "QA Reviewer")
            if not reason:
                raise ValidationError("QA disposition rationale required")
            if new_status == "Released" and row["critical_verified_by"] is None:
                raise ValidationError("critical data verification incomplete")
            if signing_user_id is None or password is None:
                raise ValidationError("QA electronic signature required")
            sig_id = self._signature(session, record_id, f"{new_status} disposition", f"status:{old}->{new_status}", signing_user_id, password)
        elif new_status == "On Hold":
            self._require_role(session, "Warehouse Operator", "QA Reviewer")
        else:
            raise AuthorizationError("transition not authorized")
        self.conn.execute("UPDATE inventory SET status=? WHERE record_id=?", (new_status, record_id))
        self._audit(session.user_id, "status_changed", record_id, "status", old, new_status, reason)
        self.conn.commit()
        return sig_id

    def classify_temperature(self, product_id: str, temperature: float) -> str:
        product = self.conn.execute("SELECT * FROM products WHERE product_id=?", (product_id,)).fetchone()
        if product is None:
            raise ValidationError("unknown product")
        lower = float(product["lower_limit"])
        upper = float(product["upper_limit"])
        is_excursion = float(temperature) < lower or float(temperature) > upper
        return "Excursion" if is_excursion else "Within range"

    def record_temperature(
        self,
        session: Session,
        record_id: str,
        temperature: float,
        event_at: str,
        source: str,
        duration_details: str | None = None,
    ) -> dict[str, Any]:
        self._require_role(session, "Warehouse Operator", "QA Reviewer")
        if not event_at or not source:
            raise ValidationError("event date/time and source/reporter information required")
        row = self._record(record_id)
        classification = self.classify_temperature(row["product_id"], temperature)
        result: dict[str, Any] = {"classification": classification, "excursion_id": None}
        if classification == "Excursion":
            cur = self.conn.execute(
                "INSERT INTO excursions(record_id,temperature,event_at,reporter,source,duration_details,classification) VALUES (?,?,?,?,?,?,?)",
                (record_id, float(temperature), event_at, session.user_id, source, duration_details, classification),
            )
            result["excursion_id"] = int(cur.lastrowid)
            self._audit(session.user_id, "excursion_created", record_id, new_value=f"excursion:{result['excursion_id']}")
            if row["status"] != "On Hold":
                self.conn.execute("UPDATE inventory SET status='On Hold' WHERE record_id=?", (record_id,))
                self._audit(session.user_id, "status_changed", record_id, "status", row["status"], "On Hold", "temperature excursion")
            self.conn.commit()
        return result

    def disposition_excursion(
        self,
        session: Session,
        record_id: str,
        final_status: str,
        rationale: str,
        signing_user_id: str,
        password: str,
    ) -> int:
        self._require_role(session, "QA Reviewer")
        if final_status not in {"Released", "Rejected"} or not rationale:
            raise ValidationError("invalid excursion disposition")
        row = self._record(record_id)
        if row["status"] != "On Hold":
            raise ValidationError("record is not on hold")
        exc = self.conn.execute(
            "SELECT * FROM excursions WHERE record_id=? AND disposition IS NULL ORDER BY id DESC LIMIT 1",
            (record_id,),
        ).fetchone()
        if exc is None:
            raise ValidationError("no unresolved excursion")
        sig_id = self._signature(session, record_id, f"{final_status} excursion disposition", f"excursion:{exc['id']}", signing_user_id, password)
        at = utc_now()
        self.conn.execute(
            "UPDATE excursions SET disposition=?, rationale=?, disposition_by=?, disposition_at=?, signature_id=? WHERE id=?",
            (final_status, rationale, session.user_id, at, sig_id, exc["id"]),
        )
        self.conn.execute("UPDATE inventory SET status=? WHERE record_id=?", (final_status, record_id))
        self._audit(session.user_id, "excursion_disposition", record_id, "status", row["status"], final_status, rationale)
        self.conn.commit()
        return sig_id

    def create_user(self, admin: Session, user_id: str, display_name: str, role: str, password: str) -> None:
        self._require_role(admin, "System Administrator")
        if role not in self.ROLES:
            raise ValidationError("unknown role")
        try:
            self.conn.execute(
                "INSERT INTO users VALUES (?,?,?,?,1)",
                (user_id, display_name, role, password_hash(password)),
            )
        except sqlite3.IntegrityError as exc:
            raise ValidationError("user identity already exists") from exc
        self.conn.execute(
            "INSERT INTO access_history(target_user,actor,at,action,old_role,new_role) VALUES (?,?,?,?,?,?)",
            (user_id, admin.user_id, utc_now(), "created", None, role),
        )
        self.conn.commit()

    def change_user_role(self, admin: Session, user_id: str, new_role: str) -> None:
        self._require_role(admin, "System Administrator")
        row = self.conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
        if row is None or new_role not in self.ROLES:
            raise ValidationError("invalid user/role")
        self.conn.execute("UPDATE users SET role=? WHERE user_id=?", (new_role, user_id))
        self.conn.execute(
            "INSERT INTO access_history(target_user,actor,at,action,old_role,new_role) VALUES (?,?,?,?,?,?)",
            (user_id, admin.user_id, utc_now(), "role_changed", row["role"], new_role),
        )
        self.conn.commit()

    def disable_user(self, admin: Session, user_id: str) -> None:
        self._require_role(admin, "System Administrator")
        row = self.conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
        if row is None:
            raise NotFoundError(user_id)
        self.conn.execute("UPDATE users SET active=0 WHERE user_id=?", (user_id,))
        self.conn.execute(
            "INSERT INTO access_history(target_user,actor,at,action,old_role,new_role) VALUES (?,?,?,?,?,?)",
            (user_id, admin.user_id, utc_now(), "disabled", row["role"], row["role"]),
        )
        self.conn.commit()

    def access_events(self, user_id: str) -> list[dict[str, Any]]:
        return [dict(r) for r in self.conn.execute("SELECT * FROM access_history WHERE target_user=? ORDER BY id", (user_id,)).fetchall()]

    def audit_events(self, record_id: str) -> list[dict[str, Any]]:
        return [dict(r) for r in self.conn.execute("SELECT * FROM audit WHERE record_id=? ORDER BY id", (record_id,)).fetchall()]

    def attempt_modify_audit(self, session: Session, audit_id: int) -> None:
        self._require_role(session, "Warehouse Operator", "QA Reviewer")
        raise AuthorizationError("ordinary users cannot alter or delete audit entries")

    def attempt_transfer_signature(self, session: Session, signature_id: int, target_record_id: str) -> None:
        self._require_role(session, "Warehouse Operator", "QA Reviewer")
        raise AuthorizationError("existing signatures cannot be transferred to another record")

    def custody_events(self, record_id: str) -> list[dict[str, Any]]:
        return [dict(r) for r in self.conn.execute("SELECT * FROM custody WHERE record_id=? ORDER BY id", (record_id,)).fetchall()]

    def signature_events(self, record_id: str) -> list[dict[str, Any]]:
        return [dict(r) for r in self.conn.execute("SELECT * FROM signatures WHERE record_id=? ORDER BY id", (record_id,)).fetchall()]

    def excursion_events(self, record_id: str) -> list[dict[str, Any]]:
        return [dict(r) for r in self.conn.execute("SELECT * FROM excursions WHERE record_id=? ORDER BY id", (record_id,)).fetchall()]

    def get_record(self, record_id: str) -> dict[str, Any]:
        return dict(self._record(record_id))

    def find_by_lot(self, lot: str) -> list[dict[str, Any]]:
        return [dict(r) for r in self.conn.execute("SELECT * FROM inventory WHERE lot=? ORDER BY created_at", (lot,)).fetchall()]

    def export_electronic(self, record_id: str) -> dict[str, Any]:
        return {
            "record": self.get_record(record_id),
            "custody": self.custody_events(record_id),
            "excursions": self.excursion_events(record_id),
            "audit": self.audit_events(record_id),
            "signatures": self.signature_events(record_id),
        }

    def export_human_readable(self, record_id: str) -> str:
        data = self.export_electronic(record_id)
        r = data["record"]
        lines = [
            f"SampleTrack record: {r['record_id']}",
            f"Product: {r['product_id']}",
            f"Lot: {r['lot']}",
            f"Quantity: {r['quantity']}",
            f"Storage condition: {r['storage_condition']}",
            f"Location: {r['location']}",
            f"Status: {r['status']}",
            f"Received by: {r['received_by']}",
            f"Created at: {r['created_at']}",
            "", "Custody history:",
        ]
        for e in data["custody"]:
            lines.append(f"- {e['at']} | {e['actor']} | {e['from_location']} -> {e['to_location']}")
        lines += ["", "Excursion history:"]
        for e in data["excursions"]:
            lines.append(f"- {e['event_at']} | {e['reporter']} | {e['temperature']} | {e['classification']} | disposition={e['disposition']} | rationale={e['rationale']}")
        lines += ["", "Audit trail:"]
        for e in data["audit"]:
            lines.append(f"- {e['at']} | {e['actor']} | {e['action']} | field={e['field']} | old={e['old_value']} | new={e['new_value']} | reason={e['reason']}")
        lines += ["", "Signatures:"]
        for s in data["signatures"]:
            lines.append(f"- {s['display_name']} ({s['actor']}) | {s['signed_at']} | {s['meaning']} | {s['action_ref']}")
        return "\n".join(lines)
