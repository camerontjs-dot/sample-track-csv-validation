# STL-RTM-001 — SampleTrack Lite Requirements Traceability Matrix

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Document ID | STL-RTM-001 |
| Title | SampleTrack Lite Requirements Traceability Matrix |
| System | SampleTrack Lite |
| Document status | Draft / pre-execution |
| URS basis | STL-URS-001 Draft, 35 requirements |
| Risk basis | STL-RSK-001 Draft, 15 risks |
| Approval status | Mock approval: Not executed |

## 1. Purpose

This matrix establishes the first lifecycle traceability path from SampleTrack user requirements to functional risks and planned OQ verification.

No OQ test has been executed at this stage.

All execution-result, evidence, deviation, and final-status fields therefore remain **NOT EXECUTED / TBD**.

## 2. Planned OQ test architecture

The identifiers below are planning anchors only. The detailed test scripts and expected results will be authored in STL-OQ-001 after the risk/traceability slice is reviewed.

| OQ ID | Planned test focus | Primary risk depth |
|---|---|---|
| OQ-TC-001 | Authentication: valid, invalid, and disabled account | V3 |
| OQ-TC-002 | Receiving record identity, required fields, creator and timestamp | V2 |
| OQ-TC-003 | Critical manual-data accuracy check | V2 |
| OQ-TC-004 | Record correction history and deletion prevention | V3 |
| OQ-TC-005 | Record retrieval, related-history integrity, and human-readable copy | V3 |
| OQ-TC-006 | Required storage condition and compatible/incompatible location assignment | V3 |
| OQ-TC-007 | Initial status and controlled configured status values | V2 |
| OQ-TC-008 | Permitted/prohibited status transitions, QA authority, and rationale | V3 |
| OQ-TC-009 | Temperature excursion lower/upper boundary values | V3 |
| OQ-TC-010 | Excursion record completeness and record linkage | V2 |
| OQ-TC-011 | Excursion hold enforcement and QA disposition | V3 |
| OQ-TC-012 | Chain-of-custody sequence and retained history | V1/V2 |
| OQ-TC-013 | Unique user identity and role-based authorization challenge | V3 |
| OQ-TC-014 | Access-authorisation creation/change/cancellation records | V3 |
| OQ-TC-015 | Audit-trail creation, content, immutability, retrieval, and reviewability | V3 |
| OQ-TC-016 | Electronic-signature manifestation and permanent record linkage | V3 |
| OQ-TC-017 | Electronic-signature identity/authentication negative challenge | V3 |
| OQ-TC-018 | End-to-end receipt → storage → custody → excursion → hold → QA disposition → retrieval | V3 |

## 3. Requirements traceability

| URS ID | Requirement focus | Risk ID(s) | Highest class | Planned OQ | Execution | Evidence | Deviation | Final status |
|---|---|---|---|---|---|---|---|---|
| URS-001 | Unique persistent inventory/receiving record ID | RSK-001 | LOW | OQ-TC-002 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-002 | Required receiving fields | RSK-002 | MEDIUM | OQ-TC-002 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-003 | Creator identity and creation date/time | RSK-015 | MEDIUM | OQ-TC-002, OQ-TC-018 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-004 | Accuracy check for critical manual receiving data | RSK-003 | MEDIUM | OQ-TC-003 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-005 | Corrections preserve prior GxP information | RSK-012 | HIGH | OQ-TC-004, OQ-TC-015 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-006 | Standard users cannot permanently delete completed GxP record | RSK-014 | HIGH | OQ-TC-004 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-007 | Retrieve by ID/lot and generate accurate complete human-readable copy | RSK-014 | HIGH | OQ-TC-005, OQ-TC-018 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-008 | Retain relationship among record and associated histories | RSK-014, RSK-012, RSK-013 | HIGH | OQ-TC-005, OQ-TC-018 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-009 | Required storage condition | RSK-004 | HIGH | OQ-TC-006 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-010 | Only compatible configured storage locations | RSK-004 | HIGH | OQ-TC-006 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-011 | Initial Quarantine status | RSK-005 | HIGH | OQ-TC-007, OQ-TC-018 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-012 | Controlled status values | RSK-005 | HIGH | OQ-TC-007 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-013 | Enforce permitted status transitions | RSK-005 | HIGH | OQ-TC-008 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-014 | QA authority required for disposition after hold/review | RSK-005, RSK-008 | HIGH | OQ-TC-008, OQ-TC-011 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-015 | Status change records user/time/prior/new/reason | RSK-005, RSK-015 | HIGH | OQ-TC-008, OQ-TC-015 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-016 | Identify out-of-range temperature excursion | RSK-006 | HIGH | OQ-TC-009 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-017 | Correct lower/upper boundary behavior | RSK-006 | HIGH | OQ-TC-009 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-018 | Excursion record completeness and affected-record linkage | RSK-007 | MEDIUM | OQ-TC-010 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-019 | Unresolved excursion remains On Hold; Warehouse Operator cannot release | RSK-008 | HIGH | OQ-TC-011, OQ-TC-018 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-020 | QA excursion disposition requires rationale and preserves history | RSK-008 | HIGH | OQ-TC-011, OQ-TC-018 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-021 | Record each custody/responsibility transfer | RSK-009 | LOW | OQ-TC-012 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-022 | Custody event user/time/prior-new information | RSK-009, RSK-015 | MEDIUM | OQ-TC-012 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-023 | New custody event does not overwrite prior history | RSK-009 | LOW | OQ-TC-012 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-024 | Unique active user identity; no shared named-user identity | RSK-010 | HIGH | OQ-TC-013 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-025 | Authentication required before GxP access | RSK-010 | HIGH | OQ-TC-001 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-026 | Functions/data changes restricted by configured role/authority | RSK-010 | HIGH | OQ-TC-013 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-027 | Disabled/cancelled account cannot authenticate | RSK-011 | HIGH | OQ-TC-001, OQ-TC-014 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-028 | Access authorisation creation/change/cancellation is recorded | RSK-011 | HIGH | OQ-TC-014 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-029 | Audit trail for risk-identified GMP actions | RSK-012 | HIGH | OQ-TC-015 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-030 | Audit trail contains user/time/record/change/values/reason | RSK-012, RSK-015 | HIGH | OQ-TC-015 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-031 | Ordinary users cannot alter/delete audit trail; changes do not obscure prior data | RSK-012 | HIGH | OQ-TC-015 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-032 | QA can retrieve/review intelligible audit trail | RSK-012 | HIGH | OQ-TC-015 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-033 | Signature shows/retains signer, date/time, and meaning | RSK-013 | HIGH | OQ-TC-016 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-034 | Signature permanently linked to record and included in human-readable output | RSK-013 | HIGH | OQ-TC-016, OQ-TC-005 | NOT EXECUTED | TBD | TBD | OPEN |
| URS-035 | Signature uses unique user identity and configured credential controls | RSK-013, RSK-010 | HIGH | OQ-TC-017 | NOT EXECUTED | TBD | TBD | OPEN |

## 4. Coverage checks

### 4.1 Requirement coverage

- URS requirements represented: **35 / 35**
- Requirements without an assigned risk: **0**
- Requirements without planned OQ coverage: **0**

### 4.2 Risk coverage

All 15 risks in STL-RSK-001 have at least one planned OQ path.

High-risk controls are generally covered by V3 tests and, where the control depends on interaction among several functions, by OQ-TC-018 as a second end-to-end path.

### 4.3 Execution status

No execution evidence exists yet.

The presence of a planned OQ ID in this matrix does **not** mean the requirement has passed.

## 5. Traceability rules for execution

When STL-OQ-001 is executed:

1. Record the actual execution result for every mapped test.
2. Add stable evidence IDs rather than vague references such as "see screenshot".
3. Link every material failed execution to STL-DL-001 / the applicable STL-DEV-### record.
4. Preserve the original failed evidence after correction.
5. Update a URS final status only after all required mapped evidence and deviations are dispositioned.
6. If a test changes materially, update the traceability relationship rather than silently substituting a new meaning under the same ID.
7. If a new risk is discovered, add it to STL-RSK-001 and reconcile affected URS/test coverage before final release disposition.

## 6. Release-critical traceability check

Before a positive VSR decision, the following High-risk paths must be directly reconstructable from this matrix:

- storage condition/location compatibility;
- material-status transition and QA authority;
- excursion detection boundaries;
- excursion hold and disposition;
- authentication/role/revoked access;
- audit-trail integrity/reviewability;
- electronic-signature identity/linkage;
- regulated-record preservation/retrieval.

A green aggregate test count is not a substitute for those paths.

## 7. Revision history

| Revision | Status | Description |
|---|---|---|
| 0.1 | Draft / pre-execution | Initial URS → risk → planned OQ traceability skeleton. |
