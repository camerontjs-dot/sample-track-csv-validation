import tempfile
import unittest
from pathlib import Path

from sampletrack import SampleTrackDemo, Session, AuthenticationError, AuthorizationError, ValidationError


class SampleTrackDemoTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.app = SampleTrackDemo(str(Path(self.tmp.name) / "db.sqlite"))
        self.credentials = {
            "WH_OP_01": "temp-wh-1",
            "WH_OP_02": "temp-wh-2",
            "QA_REVIEW_01": "temp-qa-1",
            "SYS_ADMIN_01": "temp-admin-1",
            "WH_DISABLED_01": "temp-disabled-1",
        }
        self.app.bootstrap_fixture_users(self.credentials)
        self.wh = self.app.authenticate("WH_OP_01", self.credentials["WH_OP_01"])
        self.qa = self.app.authenticate("QA_REVIEW_01", self.credentials["QA_REVIEW_01"])

    def tearDown(self):
        self.app.close()
        self.tmp.cleanup()

    def record(self, lot="LOT-U-001"):
        return self.app.create_inventory(self.wh, "DEMO-RX-COLD-001", lot, 24, "REFRIGERATED_2_8C")

    def test_authentication_and_disabled_account(self):
        with self.assertRaises(AuthenticationError):
            self.app.authenticate("WH_OP_01", "wrong")
        with self.assertRaises(AuthenticationError):
            self.app.authenticate("WH_DISABLED_01", self.credentials["WH_DISABLED_01"])

    def test_unique_records(self):
        self.assertNotEqual(self.record("LOT-U-001"), self.record("LOT-U-002"))

    def test_incompatible_location_rejected(self):
        rid = self.record()
        with self.assertRaises(ValidationError):
            self.app.assign_location(self.wh, rid, "CRT-A1")
        self.app.assign_location(self.wh, rid, "REFR-A1")
        self.assertEqual(self.app.get_record(rid)["location"], "REFR-A1")

    def test_warehouse_cannot_release(self):
        rid = self.record()
        self.app.verify_critical_data(self.qa, rid, "DEMO-RX-COLD-001", "LOT-U-001", "REFRIGERATED_2_8C")
        with self.assertRaises(AuthorizationError):
            self.app.transition_status(self.wh, rid, "Released", "release", "WH_OP_01", self.credentials["WH_OP_01"])

    def test_excursion_places_record_on_hold(self):
        rid = self.record()
        result = self.app.record_temperature(self.wh, rid, 8.1, "2026-09-30T12:00:00Z", "mock logger", "10 min")
        self.assertEqual(result["classification"], "Excursion")
        self.assertEqual(self.app.get_record(rid)["status"], "On Hold")

    def test_inclusive_upper_temperature_boundary_is_within_range(self):
        rid = self.record()
        result = self.app.record_temperature(self.wh, rid, 8.0, "2026-09-30T12:00:00Z", "mock logger", "10 min")
        self.assertEqual(result["classification"], "Within range")
        self.assertEqual(self.app.get_record(rid)["status"], "Quarantine")

    def test_audit_cannot_be_modified_by_ordinary_user(self):
        rid = self.record()
        event_id = self.app.audit_events(rid)[0]["id"]
        with self.assertRaises(AuthorizationError):
            self.app.attempt_modify_audit(self.wh, event_id)

    def test_signature_requires_correct_credentials(self):
        rid = self.record()
        self.app.verify_critical_data(self.qa, rid, "DEMO-RX-COLD-001", "LOT-U-001", "REFRIGERATED_2_8C")
        with self.assertRaises(AuthenticationError):
            self.app.transition_status(self.qa, rid, "Released", "QA review complete", "QA_REVIEW_01", "wrong")
        self.app.transition_status(self.qa, rid, "Released", "QA review complete", "QA_REVIEW_01", self.credentials["QA_REVIEW_01"])
        self.assertEqual(self.app.get_record(rid)["status"], "Released")
        self.assertEqual(len(self.app.signature_events(rid)), 1)


    def test_unauthenticated_gxp_write_is_controlled_denial(self):
        with self.assertRaises(AuthenticationError):
            self.app.create_inventory(None, "DEMO-RX-COLD-001", "LOT-UNAUTH", 1, "REFRIGERATED_2_8C")

    def test_forged_session_cannot_authorize_gxp_write(self):
        forged = Session("WH_OP_01", "Warehouse Operator", "FORGED-TOKEN")
        with self.assertRaises(AuthenticationError):
            self.app.create_inventory(forged, "DEMO-RX-COLD-001", "LOT-FORGED", 1, "REFRIGERATED_2_8C")


if __name__ == "__main__":
    unittest.main()
