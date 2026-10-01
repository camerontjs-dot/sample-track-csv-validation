import math
import tempfile
import unittest
from pathlib import Path

from sampletrack import SampleTrackDemo, AuthenticationError, ValidationError


class PublicPressureTests(unittest.TestCase):
    """Adversarial requirement tests added before public release.

    These tests intentionally challenge behavior that the final 18-case OQ did not
    exercise directly. They are not part of the frozen OQ oracle.
    """

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.app = SampleTrackDemo(str(Path(self.tmp.name) / "pressure.sqlite"))
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
        self.admin = self.app.authenticate("SYS_ADMIN_01", self.credentials["SYS_ADMIN_01"])

    def tearDown(self):
        self.app.close()
        self.tmp.cleanup()

    def record(self, lot="LOT-PRESSURE-001"):
        return self.app.create_inventory(
            self.wh,
            "DEMO-RX-COLD-001",
            lot,
            24,
            "REFRIGERATED_2_8C",
        )

    def test_critical_verification_is_invalidated_after_critical_lot_correction(self):
        """URS-004: release must rely on verification of current critical data."""
        rid = self.record()
        self.assertTrue(
            self.app.verify_critical_data(
                self.qa,
                rid,
                "DEMO-RX-COLD-001",
                "LOT-PRESSURE-001",
                "REFRIGERATED_2_8C",
            )
        )
        self.app.correct_field(
            self.wh,
            rid,
            "lot",
            "LOT-PRESSURE-001-CORRECTED",
            "pressure-test critical correction",
        )
        with self.assertRaises(ValidationError):
            self.app.transition_status(
                self.qa,
                rid,
                "Released",
                "QA release after changed critical data",
                "QA_REVIEW_01",
                self.credentials["QA_REVIEW_01"],
            )

    def test_gmp_status_change_requires_reason(self):
        """URS-015: a GMP-relevant status change requires a reason/rationale."""
        rid = self.record()
        with self.assertRaises(ValidationError):
            self.app.transition_status(self.wh, rid, "On Hold")

    def test_same_status_request_does_not_bypass_authentication(self):
        """URS-025: authentication precedes access to the status function."""
        rid = self.record()
        with self.assertRaises(AuthenticationError):
            self.app.transition_status(None, rid, "Quarantine")

    def test_record_retrieval_is_not_available_without_authenticated_authority(self):
        """URS-007/025: regulated-record retrieval is an authorized-user function."""
        rid = self.record()
        record = self.app.get_record(rid)
        self.fail(
            "Unauthenticated get_record returned regulated data: "
            + str({"record_id": record["record_id"], "lot": record["lot"]})
        )

    def test_disabled_user_existing_session_is_invalidated(self):
        rid = self.record("LOT-PRESSURE-SESSION")
        self.app.disable_user(self.admin, "WH_OP_01")
        with self.assertRaises(AuthenticationError):
            self.app.assign_location(self.wh, rid, "REFR-A1")

    def test_role_change_invalidates_existing_session(self):
        rid = self.record("LOT-PRESSURE-ROLE")
        self.app.change_user_role(self.admin, "WH_OP_01", "QA Reviewer")
        with self.assertRaises(AuthenticationError):
            self.app.assign_location(self.wh, rid, "REFR-A1")


if __name__ == "__main__":
    unittest.main()
