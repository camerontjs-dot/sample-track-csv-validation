# STL-OQ-001 Execution Record

> MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE

- Execution ID: OQ-CI-36947930824
- Tester: Cameron
- System identity: c3463a18b18c359d4d639055c4e3f6121df79f80
- Executed at: 2026-10-02T00:49:49+00:00
- Result: 18 PASS / 0 FAIL

## OQ-TC-001 — Valid, invalid, and disabled authentication

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| unauthenticated GxP access | Controlled access denial | Rejected as expected: AuthenticationError: authenticated session required | PASS |
| valid password | Warehouse session established | WH_OP_01/Warehouse Operator | PASS |
| invalid password | Authentication rejected | Rejected as expected: AuthenticationError: authentication failed | PASS |
| GxP access after invalid authentication | No data-changing operation permitted | Rejected as expected: AuthenticationError: authenticated session required | PASS |
| disabled account | Authentication rejected | Rejected as expected: AuthenticationError: authentication failed | PASS |
| GxP access after disabled authentication | No data-changing operation permitted | Rejected as expected: AuthenticationError: authenticated session required | PASS |

Evidence: STL-EV-OQ-001-01

## OQ-TC-002 — Receiving record identity, required fields, creator/time

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| missing lot | Completion blocked | Rejected as expected: ValidationError: required receiving fields missing | PASS |
| complete record | Valid record completes | STL-2AD9697379E1 | PASS |
| generated identifier | Non-empty SampleTrack ID assigned | STL-2AD9697379E1 | PASS |
| persistent ID | Same ID on retrieval | STL-2AD9697379E1 | PASS |
| creator/time | WH_OP_01 and creation time recorded | WH_OP_01 @ 2026-10-02T00:49:48+00:00 | PASS |
| second identity | Different unique ID | STL-2AD9697379E1 != STL-F09F2ABDA952 | PASS |

Evidence: STL-EV-OQ-002-01

## OQ-TC-003 — Critical manual-data accuracy check

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| release before verification | Release blocked | Rejected as expected: ValidationError: critical data verification incomplete | PASS |
| matching verification | Complete and attributable | True/QA_REVIEW_01 | PASS |
| verification state retained | QA verifier and timestamp retained | QA_REVIEW_01 @ 2026-10-02T00:49:48+00:00 | PASS |
| discrepant verification | Does not complete | False | PASS |
| release after mismatch | Release blocked | Rejected as expected: ValidationError: critical data verification incomplete | PASS |

Evidence: STL-EV-OQ-003-01

## OQ-TC-004 — Correction history and deletion prevention

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| permitted correction | Current value updated | LOT-OQ-001A | PASS |
| correction history | Prior/new/reason/user/time retained | {"action": "record_corrected", "actor": "WH_OP_01", "at": "2026-10-02T00:49:48+00:00", "field": "lot", "id": 2, "new_value": "LOT-OQ-001A", "old_value": "LOT-OQ-001", "reason": "transcription correction", "record_id": "STL-406EEF843636"} | PASS |
| Warehouse delete | Denied | Rejected as expected: AuthorizationError: permanent deletion of completed GxP record is not permitted | PASS |
| QA delete | Denied | Rejected as expected: AuthorizationError: permanent deletion of completed GxP record is not permitted | PASS |
| record retained | Record and correction retained | LOT-OQ-001A | PASS |

Evidence: STL-EV-OQ-004-01

## OQ-TC-005 — Record retrieval, related history, and record copies

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| retrieve by ID | Correct record | STL-288933C48287 | PASS |
| retrieve by lot | Same record unambiguous | ['STL-288933C48287'] | PASS |
| related history | History linked | custody=1;audit=2 | PASS |
| human-readable copy | Readable record/history copy | SampleTrack record: STL-288933C48287 \| Product: DEMO-RX-COLD-001 \| Lot: LOT-OQ-001 \| Quantity: 24 \| Storage condition: REFRIGERATED_2_8C \| Location: REFR-A1 \| Status: Quarantine \| Received by: W | PASS |
| electronic copy | Accurate structured copy | ['audit', 'custody', 'excursions', 'record', 'signatures'] | PASS |
| copy comparison | Both outputs preserve tested record values and meaning | True | PASS |

Evidence: STL-EV-OQ-005-01, STL-EV-OQ-005-02

## OQ-TC-006 — Storage condition/location compatibility

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| required condition | REFRIGERATED_2_8C | REFRIGERATED_2_8C | PASS |
| compatible | REFR-A1 accepted | REFR-A1 | PASS |
| incompatible | CRT-A1 rejected | Rejected as expected: ValidationError: location incompatible with required storage condition | PASS |
| inactive | RETIRED-R1 rejected | Rejected as expected: ValidationError: location is inactive or unknown | PASS |
| second compatible | REFR-A2 accepted with retained history | REFR-A2/2 | PASS |

Evidence: STL-EV-OQ-006-01

## OQ-TC-007 — Initial and controlled material statuses

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| initial status | Quarantine | Quarantine | PASS |
| controlled values | Six configured values present | ['On Hold', 'Quarantine', 'Recalled', 'Rejected', 'Released', 'Returned'] | PASS |
| free-text status | Rejected | Rejected as expected: ValidationError: unconfigured status | PASS |
| valid state retained | Quarantine | Quarantine | PASS |

Evidence: STL-EV-OQ-007-01

## OQ-TC-008 — Status sequencing, QA authority, and rationale

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| Warehouse release | Denied | Rejected as expected: AuthorizationError: Warehouse Operator not authorized | PASS |
| QA release without rationale | Denied | Rejected as expected: ValidationError: QA disposition rationale required | PASS |
| QA release | Released | Released | PASS |
| status history | Prior/new/user/time/rationale retained | {"action": "status_changed", "actor": "QA_REVIEW_01", "at": "2026-10-02T00:49:49+00:00", "field": "status", "id": 4, "new_value": "Released", "old_value": "Quarantine", "reason": "QA review complete", "record_id": "STL-FD2CC81E1F6B"} | PASS |
| prohibited sequence | Rejected | Rejected as expected: ValidationError: prohibited status transition | PASS |

Evidence: STL-EV-OQ-008-01

## OQ-TC-009 — Temperature lower/upper boundary behavior

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| 1.9 C | Excursion | Excursion | PASS |
| 2.0 C | Within range | Within range | PASS |
| 2.1 C | Within range | Within range | PASS |
| 7.9 C | Within range | Within range | PASS |
| 8.0 C | Within range | Within range | PASS |
| 8.1 C | Excursion | Excursion | PASS |

Evidence: STL-EV-OQ-009-01

## OQ-TC-010 — Excursion-record completeness and linkage

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| missing source | Rejected | Rejected as expected: ValidationError: event date/time and source/reporter information required | PASS |
| complete excursion | Saved | Excursion/1 | PASS |
| retrieve affected record | Excursion linked to correct inventory record | STL-E10C87FDC6C8 | PASS |
| excursion content | Required content retained | {"classification": "Excursion", "disposition": null, "disposition_at": null, "disposition_by": null, "duration_details": "10 min", "event_at": "2026-09-30T12:00:00+00:00", "id": 1, "rationale": null, "record_id": "STL-E10C87FDC6C8", "reporter": "WH_OP_01", "signature_id": null, "source": "mock logger", "temperature": 8.1} | PASS |
| excursion reread | Same event identity and content returned | 1 | PASS |

Evidence: STL-EV-OQ-010-01

## OQ-TC-011 — Excursion hold enforcement and QA disposition

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| excursion hold | On Hold | On Hold | PASS |
| Warehouse release | Denied | Rejected as expected: AuthorizationError: Warehouse Operator not authorized | PASS |
| QA no rationale | Denied | Rejected as expected: ValidationError: invalid excursion disposition | PASS |
| QA disposition | Released with rationale/signature | Released/sig=2 | PASS |
| excursion/disposition history | Excursion, QA identity/time, rationale, status and signature retained | {"classification": "Excursion", "disposition": "Released", "disposition_at": "2026-10-02T00:49:49+00:00", "disposition_by": "QA_REVIEW_01", "duration_details": "10 min", "event_at": "2026-09-30T12:00:00+00:00", "id": 1, "rationale": "mock technical disposition: acceptable for workflow test", "record_id": "STL-8B3AEC7E65A6", "reporter": "WH_OP_01", "signature_id": 2, "source": "mock logger", "temperature": 8.1} | PASS |

Evidence: STL-EV-OQ-011-01

## OQ-TC-012 — Chain-of-custody history

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| first event | WH_OP_01 to REFR-A1 with time | {"actor": "WH_OP_01", "at": "2026-10-02T00:49:49+00:00", "from_location": null, "id": 1, "record_id": "STL-871EDF20C6B5", "to_location": "REFR-A1"} | PASS |
| second event | WH_OP_02 REFR-A1 to REFR-A2 | {"actor": "WH_OP_02", "at": "2026-10-02T00:49:49+00:00", "from_location": "REFR-A1", "id": 2, "record_id": "STL-871EDF20C6B5", "to_location": "REFR-A2"} | PASS |
| custody history retrieval | Both chronological events retained | [1, 2] | PASS |
| current record state | Latest location without history loss | REFR-A2/2 | PASS |

Evidence: STL-EV-OQ-012-01

## OQ-TC-013 — Unique identity and role-based authorization

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| duplicate identity | Rejected | Rejected as expected: ValidationError: user identity already exists | PASS |
| Warehouse QA action | Denied | Rejected as expected: AuthorizationError: Warehouse Operator not authorized | PASS |
| Warehouse admin | Denied | Rejected as expected: AuthorizationError: Warehouse Operator not authorized | PASS |
| QA admin | Denied | Rejected as expected: AuthorizationError: QA Reviewer not authorized | PASS |
| Admin QA action | Denied | Rejected as expected: AuthorizationError: System Administrator not authorized | PASS |

Evidence: STL-EV-OQ-013-01

## OQ-TC-014 — Access-authorisation lifecycle record

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| access creation | Creation event recorded | {"action": "created", "actor": "SYS_ADMIN_01", "at": "2026-10-02T00:49:49+00:00", "id": 1, "new_role": "Warehouse Operator", "old_role": null, "target_user": "TEMP_ACCESS_01"} | PASS |
| access change | Role change recorded | {"action": "role_changed", "actor": "SYS_ADMIN_01", "at": "2026-10-02T00:49:49+00:00", "id": 2, "new_role": "QA Reviewer", "old_role": "Warehouse Operator", "target_user": "TEMP_ACCESS_01"} | PASS |
| access history review | What changed, when, and acting admin attributable | [{"action": "created", "actor": "SYS_ADMIN_01", "at": "2026-10-02T00:49:49+00:00", "id": 1, "new_role": "Warehouse Operator", "old_role": null, "target_user": "TEMP_ACCESS_01"}, {"action": "role_changed", "actor": "SYS_ADMIN_01", "at": "2026-10-02T00:49:49+00:00", "id": 2, "new_role": "QA Reviewer", "old_role": "Warehouse Operator", "target_user": "TEMP_ACCESS_01"}] | PASS |
| access cancellation | Disable event recorded | {"action": "disabled", "actor": "SYS_ADMIN_01", "at": "2026-10-02T00:49:49+00:00", "id": 3, "new_role": "QA Reviewer", "old_role": "QA Reviewer", "target_user": "TEMP_ACCESS_01"} | PASS |
| disabled login | Rejected | Rejected as expected: AuthenticationError: authentication failed | PASS |

Evidence: STL-EV-OQ-014-01

## OQ-TC-015 — Audit-trail coverage, content, immutability, reviewability

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| creation/correction audit | Creation and correction events present | ['record_corrected', 'record_created'] | PASS |
| status-change audit | Status change represented | ['record_created', 'record_corrected', 'critical_verification_complete', 'electronic_signature', 'status_changed'] | PASS |
| excursion/disposition/signature audit | Risk-relevant events represented | ['critical_verification_complete', 'electronic_signature', 'excursion_created', 'excursion_disposition', 'record_corrected', 'record_created', 'status_changed'] | PASS |
| change content | User/time/prior/new/reason | {"action": "record_corrected", "actor": "WH_OP_01", "at": "2026-10-02T00:49:49+00:00", "field": "lot", "id": 2, "new_value": "LOT-OQ-001A", "old_value": "LOT-OQ-001", "reason": "transcription correction", "record_id": "STL-AD53C82C7EDF"} | PASS |
| audit modification | Denied | Rejected as expected: AuthorizationError: ordinary users cannot alter or delete audit entries | PASS |
| QA reviewability | QA Reviewer can retrieve a chronological intelligible trail | 9 events | PASS |
| known-action comparison | Sequence attributable and prior value not obscured | ['record_created', 'record_corrected', 'critical_verification_complete', 'electronic_signature', 'status_changed', 'excursion_created', 'status_changed', 'electronic_signature', 'excursion_disposition'] | PASS |

Evidence: STL-EV-OQ-015-01

## OQ-TC-016 — Electronic-signature manifestation and record linkage

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| signature completion | Linked to signed record | 1/STL-01A5475CA278 | PASS |
| manifestation | Name/time/meaning present | {"action_ref": "status:Quarantine->Released", "actor": "QA_REVIEW_01", "display_name": "Mock QA Reviewer 01", "id": 1, "meaning": "Released disposition", "record_id": "STL-01A5475CA278", "signed_at": "2026-10-02T00:49:49+00:00"} | PASS |
| persistent linkage | Same signature after retrieval | [1] | PASS |
| human-readable signature | Signature included | 9:49+00:00 \| QA_REVIEW_01 \| status_changed \| field=status \| old=Quarantine \| new=Released \| reason=QA release \|  \| Signatures: \| - Mock QA Reviewer 01 (QA_REVIEW_01) \| 2026-10-02T00:49:49+00:00 \| Released disposition \| status:Quarantine->Released | PASS |
| signature transfer | Denied/no target signature | Rejected as expected: AuthorizationError: existing signatures cannot be transferred to another record | PASS |

Evidence: STL-EV-OQ-016-01

## OQ-TC-017 — Electronic-signature identity and credential challenge

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| wrong password | Rejected | Rejected as expected: AuthenticationError: signature authentication failed | PASS |
| failed signature leaves protected state | No signature and no completed disposition | status=Quarantine;signatures=0 | PASS |
| different ID code | Rejected/no disposition | Rejected as expected: AuthenticationError: signature identity does not match authenticated user | PASS |
| Warehouse signed action | Denied | Rejected as expected: AuthorizationError: Warehouse Operator not authorized | PASS |
| correct QA credentials | Signature/action succeeds | Released | PASS |
| signature attribution | Attributed to QA_REVIEW_01 | QA_REVIEW_01 | PASS |

Evidence: STL-EV-OQ-017-01

## OQ-TC-018 — End-to-end regulated workflow

Result: PASS

| Step | Expected | Actual | Result |
|---|---|---|---|
| receive | Unique Quarantine record | STL-CA4A54C5AABC/Quarantine | PASS |
| critical verification | Attributable QA verification | True/QA_REVIEW_01 | PASS |
| location/release | Compatible location and signed release | REFR-A1/Released | PASS |
| custody transfer | Second event appended | 2 | PASS |
| 8.1 C excursion | Excursion and On Hold | Excursion/On Hold | PASS |
| Warehouse re-release | Denied | Rejected as expected: AuthorizationError: Warehouse Operator not authorized | PASS |
| QA excursion disposition | Signed release | Released | PASS |
| linked final history | All history linked | custody=2;excursions=1;audit=10;signatures=2 | PASS |
| human-readable output | Record and signatures present | SampleTrack record: STL-CA4A54C5AABC \| Product: DEMO-RX-COLD-001 \| Lot: LOT-OQ-004 \| Quantity: 24 \| Storage condition: REFRIGERATED_2_8C \| Location: REFR-A2 \| Status: Released \| Received by: WH_OP_01 \| Receipt date: 2026-09-30 \| Created a | PASS |
| sequence reconstruction | Creation/excursion/disposition reconstructable | ['record_created', 'critical_verification_complete', 'location_changed', 'electronic_signature', 'status_changed', 'location_changed', 'excursion_created', 'status_changed', 'electronic_signature', 'excursion_disposition'] | PASS |

Evidence: STL-EV-OQ-018-01
