# STL-CR-001 — Change Request: DEV-001 Upper Temperature Boundary Correction

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**
>
> **SAMPLE CHANGE-REQUEST RECORD.** All approvals are `UNSIGNED – MOCK`. This record was written on 2026-10-01 from the STL-DL-001 DEV-001 entry and the repository history, after the change had already been made and verified. In a real change-control system it would be raised, assessed, and approved before implementation.

| Field | Value |
|---|---|
| Change request ID | STL-CR-001 |
| Title | Correct inclusive upper temperature boundary in excursion classification |
| System | SampleTrack Lite demonstration surrogate |
| Change type | Corrective (deviation-driven) |
| Source deviation | STL-DL-001 DEV-001 |
| Status | Implemented and verified (mock) |
| Approval status | Mock approval blocks only, `UNSIGNED – MOCK` |

## 1. Reason for change

The initial OQ execution `OQ-EXEC-001` (GitHub Actions run `36812149305`, candidate `e1636c513661a8d6784e9594f8929b1592b690c7`) returned 17 PASS / 1 FAIL. In `OQ-TC-009` the frozen input 8.0 °C was expected to be `Within range` and was classified as `Excursion`. The frozen `REFRIGERATED_2_8C` oracle defines the upper limit as 8.0 °C inclusive.

DEV-001 classified this as a system / configuration failure.

## 2. Description of change

| Item | Before | After |
|---|---|---|
| File | `demo/sampletrack.py` | `demo/sampletrack.py` |
| Upper-bound comparison | `temperature >= upper_limit` | `temperature > upper_limit` |
| Development test | none for 8.0 °C | `test_inclusive_upper_temperature_boundary_is_within_range` added to `demo/test_sampletrack.py` |

Not changed: the frozen 8.0 °C expected result, STL-OQ-001, the test configuration and data set, STL-URS-001, and every other frozen validation artifact.

## 3. Impact assessment

| Area | Assessment |
|---|---|
| Requirements | URS-016, URS-017 |
| Risk | RSK-006, HIGH (S5 / P3 / D5, RPN 75). Design-time score not changed. |
| OQ cases affected | OQ-TC-009 directly. OQ-TC-018 uses the same comparison path, so regression is required. |
| Frozen authority | None changed. The correction brings the system to the frozen oracle, not the other way around. |
| Data / records | Demonstration data only. A real system would also need a review of records classified while the defect was present. |
| Other functions | Inside the application, `classify_temperature` is called only from `record_temperature`, the excursion workflow entry point. |

## 4. Verification plan

Full re-execution of the frozen OQ was chosen over a partial rerun of OQ-TC-009 and OQ-TC-018, because the automated run is cheap and gives stronger regression evidence (STL-DL-001 DEV-001, "Re-test requirement").

Acceptance: all six frozen boundary inputs return their frozen expected results, development tests pass, and the full OQ passes with no change to expected results.

## 5. Implementation and verification record

| Item | Value |
|---|---|
| Fix commit | `f365708` "fix: honor inclusive upper temperature boundary" (2026-09-30 23:50 ET) |
| Test commit | `7a8f114bfd67935d8354e922873fa54f0a2c37c9` "test: guard inclusive upper temperature boundary" (2026-09-30 23:50 ET) |
| Verified candidate | `7a8f114bfd67935d8354e922873fa54f0a2c37c9`, tree `07182c62c251f767ccfde481816d5f22a84daecc` |
| Verification run | GitHub Actions run `36812375284`, job `110210033595` |
| Development tests | 8 / 8 PASS |
| Frozen OQ | 18 / 18 PASS, including 8.0 °C → Within range and 8.1 °C → Excursion |
| Corrected `sampletrack.py` SHA-256 | `96c033656393a8a7f8896dfe9ac8cd868895f4aae8ce52999ea20f41d6ae3ddb` |
| Retest artifact | `11139822400`, digest `sha256:95739a76b983693e2d438ee1eecbc7584fdbf2aba16b2d7e9cfc08ea76d45d78` |

All values above are copied from STL-DL-001 DEV-001 and the Git history of this repository.

## 6. Closure

The change met its acceptance criteria. Final package closure for this behavior also depended on DEV-002, DEV-003, and DEV-004, which required later full OQ reruns. The current release authority remains `OQ-CI-36947930824` (see STL-VSR-001).

The original failed run and evidence remain preserved.

## 7. Mock approvals

| Signatory role | Name | Date | Meaning of signature | Signature |
|---|---|---|---|---|
| Author (validation lead / exercise owner) | Not entered (mock) | YYYY-MM-DD, not signed | I prepared this document and confirm it is accurate and complete for its stated scope. | `UNSIGNED – MOCK` |
| Reviewer (technical / process SME) | Not entered (mock) | YYYY-MM-DD, not signed | I reviewed this document for technical accuracy, consistency with upstream documents, and traceability. | `UNSIGNED – MOCK` |
| QA Approver (Quality Assurance) | Not entered (mock) | YYYY-MM-DD, not signed | I approve this document for use within the bounded mock validation package. | `UNSIGNED – MOCK` |

## 8. Revision history

| Revision | Status | Description |
|---|---|---|
| 1.0 | Implemented and verified (mock) | Sample change-request record for the DEV-001 correction, written retrospectively from STL-DL-001 and Git history. |
