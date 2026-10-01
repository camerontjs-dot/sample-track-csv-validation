# STL-OQ-001 — Test Configuration and Data Set

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Parent protocol | STL-OQ-001 |
| Artifact purpose | Predeclared configuration and test-data authority |
| Status | Draft / pre-execution |
| Approval status | Mock approval: Not executed |

## 1. Purpose

This file defines the fictional configuration and stable test data used by the SampleTrack Lite OQ protocol.

The values below are **test fixtures**, not specifications for any real drug, warehouse, product, customer, or employer.

They are frozen before execution so a failing OQ result cannot be repaired by silently moving a limit, changing a role, or redefining an allowed workflow.

## 2. User fixtures

No passwords, secrets, or real credentials may be committed to the repository.

| User ID | Display name | Role | Initial state |
|---|---|---|---|
| WH_OP_01 | Mock Warehouse Operator 01 | Warehouse Operator | Active |
| WH_OP_02 | Mock Warehouse Operator 02 | Warehouse Operator | Active |
| QA_REVIEW_01 | Mock QA Reviewer 01 | QA Reviewer | Active |
| SYS_ADMIN_01 | Mock System Administrator 01 | System Administrator | Active |
| WH_DISABLED_01 | Mock Disabled Warehouse Operator | Warehouse Operator | Disabled |

### Role authority

**Warehouse Operator**

May:

- create receiving/inventory records;
- enter permitted receiving data;
- assign compatible configured storage locations;
- record permitted custody events;
- report/record excursion observations;
- view records within scope.

May not:

- perform QA release/reject disposition;
- remove On Hold caused by unresolved excursion;
- administer accounts or roles;
- alter/delete audit-trail records;
- apply a QA electronic signature.

**QA Reviewer**

May:

- perform critical-data verification;
- review GxP record history;
- perform configured QA disposition;
- enter disposition rationale;
- apply QA electronic signature;
- review audit trails.

May not:

- administer user accounts/roles;
- alter/delete audit-trail entries by ordinary means.

**System Administrator**

May:

- create, change, disable, and administer mock users/roles;
- maintain permitted application configuration within the fictional controlled-change model.

May not, merely by virtue of technical administration:

- perform QA disposition;
- apply a QA electronic signature.

## 3. Product fixtures

| Product ID | Description | Required storage condition |
|---|---|---|
| DEMO-RX-COLD-001 | Fictional refrigerated demonstration product | REFRIGERATED_2_8C |
| DEMO-RX-ROOM-001 | Fictional room-temperature demonstration product | CONTROLLED_ROOM_15_25C |

## 4. Storage-condition fixtures

### REFRIGERATED_2_8C

For this fictional test configuration:

- lower acceptable limit: **2.0 °C inclusive**
- upper acceptable limit: **8.0 °C inclusive**
- any value **< 2.0 °C** or **> 8.0 °C** is an excursion condition.

This range is selected only to make boundary behavior easy to test. It is not asserted as the approved storage condition of any real product.

### CONTROLLED_ROOM_15_25C

For this fictional test configuration:

- lower acceptable limit: **15.0 °C inclusive**
- upper acceptable limit: **25.0 °C inclusive**
- any value **< 15.0 °C** or **> 25.0 °C** is an excursion condition.

## 5. Storage-location fixtures

| Location | Permitted condition | Active |
|---|---|---|
| REFR-A1 | REFRIGERATED_2_8C | Yes |
| REFR-A2 | REFRIGERATED_2_8C | Yes |
| CRT-A1 | CONTROLLED_ROOM_15_25C | Yes |
| RETIRED-R1 | REFRIGERATED_2_8C | No |

An active inventory record may be assigned only to an **active location compatible with its required storage condition**.

## 6. Material-status fixtures

Configured status values:

- Quarantine
- Released
- On Hold
- Rejected
- Returned
- Recalled

Free-text or unconfigured status values are not permitted.

### Initial status

A newly completed receiving record enters **Quarantine**.

### Principal transition rules

| From | To | Authority / prerequisite |
|---|---|---|
| Quarantine | Released | QA Reviewer; critical-data verification complete; rationale; QA e-signature |
| Quarantine | On Hold | Permitted workflow/system event |
| Quarantine | Rejected | QA Reviewer; rationale; QA e-signature |
| Released | On Hold | Permitted workflow/system event, including excursion |
| On Hold | Released | QA Reviewer; unresolved cause dispositioned; rationale; QA e-signature |
| On Hold | Rejected | QA Reviewer; rationale; QA e-signature |
| Released | Recalled | QA Reviewer; rationale; QA e-signature |

Warehouse Operator cannot directly set **Released**, **Rejected**, or **Recalled**.

An unresolved excursion keeps affected material **On Hold**.

## 7. Critical manual-data verification

The following receiving fields are treated as critical in the mock workflow:

- product/material identifier;
- lot/batch number;
- required storage condition.

Before material can enter **Released** from its initial Quarantine state, a QA Reviewer must verify those critical values.

The verification result must remain attributable to the QA Reviewer and the relevant record.

## 8. Receiving test data

Primary record fixture:

| Field | Value |
|---|---|
| Product | DEMO-RX-COLD-001 |
| Lot/batch | LOT-OQ-001 |
| Quantity | 24 |
| Required storage | REFRIGERATED_2_8C |
| Receiving user | WH_OP_01 |
| Intended compatible location | REFR-A1 |
| Initial status | Quarantine |

Secondary record fixtures may use:

- LOT-OQ-002
- LOT-OQ-003
- LOT-OQ-004

Each test must record the actual generated SampleTrack record ID so evidence remains traceable.

## 9. Temperature boundary test values

For **REFRIGERATED_2_8C**:

| Input | Expected classification |
|---:|---|
| 1.9 °C | Excursion |
| 2.0 °C | Within range |
| 2.1 °C | Within range |
| 7.9 °C | Within range |
| 8.0 °C | Within range |
| 8.1 °C | Excursion |

These exact values are frozen before OQ execution.

## 10. Electronic-signature fixture

For this exercise, a QA electronic signature:

- is executed only by QA_REVIEW_01 for defined QA actions;
- is bound to the currently authenticated unique QA user identity;
- requires entry of QA_REVIEW_01's configured identification code and password for each signing action;
- records the signer's displayed name;
- records date/time;
- records the meaning of the signing action;
- remains linked to the signed record/action;
- appears with the signed record in human-readable output.

Actual passwords are provisioned locally and are not versioned.

This is a demonstration configuration. It does not establish an FDA certification or legal non-repudiation process.

## 11. Audit-trail event set

The OQ expects the system-generated audit history to cover, as applicable:

- receiving record creation;
- permitted GMP-relevant data correction;
- material-status change;
- excursion creation;
- QA excursion disposition;
- QA electronic signature;
- user-access authorization creation/change/cancellation.

The required audit content depends on the event, but the OQ will challenge attribution, date/time, affected record/object, action/change, prior/new values where applicable, and reason where required.

## 12. Time and date handling

The test executor records the actual execution date/time.

The demonstration environment must expose a stable date/time source sufficient to compare the observed action with the recorded system event.

This protocol does not establish enterprise time-synchronization qualification.

## 13. Test independence and reuse

Tests may reuse records from an earlier test only when:

- the prior test completed to a known state;
- the exact SampleTrack record ID is recorded;
- reuse cannot hide the behavior under test;
- the OQ actual-result field identifies the reused record.

When those conditions are not met, create a dedicated test record.

## 14. Revision history

| Revision | Status | Description |
|---|---|---|
| 0.1 | Draft / pre-execution | Initial frozen candidate configuration and test-data set. |
| 0.2 | Draft / pre-execution | Pre-OQ source review: made the non-biometric signature credential rule explicit for every signing action. |
