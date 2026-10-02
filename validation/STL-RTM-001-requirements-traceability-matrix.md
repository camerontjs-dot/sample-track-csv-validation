# STL-RTM-001 — SampleTrack Lite Requirements Traceability Matrix

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Document ID | STL-RTM-001 |
| Title | SampleTrack Lite Requirements Traceability Matrix |
| System | SampleTrack Lite |
| Document status | Executed / reconciled |
| URS basis | STL-URS-001 Draft, 35 requirements |
| Risk basis | STL-RSK-001 Draft, 15 risks |
| Approval status | Mock approval: Not executed |

## 1. Purpose

This matrix records lifecycle traceability from SampleTrack user requirements to functional risks, executed OQ verification, evidence, deviations, and final requirement status for the qualified mock candidate `b528234a0a14db68200c9213516d0ed6a76ca56b`.

Final execution authority: `OQ-CI-36947244505`, GitHub Actions run `36813357212`, frozen OQ result **18 / 18 PASS**.

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
| URS-001 | Unique persistent inventory/receiving record ID | RSK-001 | LOW | OQ-TC-002 | PASS — OQ-CI-36947244505 | STL-EV-OQ-002-01 | None | VERIFIED — PASS |
| URS-002 | Required receiving fields | RSK-002 | MEDIUM | OQ-TC-002 | PASS — OQ-CI-36947244505 | STL-EV-OQ-002-01 + receipt-date pressure test | DEV-011 (resolved) | VERIFIED — PASS |
| URS-003 | Creator identity and creation date/time | RSK-015 | MEDIUM | OQ-TC-002, OQ-TC-018 | PASS — OQ-CI-36947244505 | STL-EV-OQ-002-01, STL-EV-OQ-018-01 | None | VERIFIED — PASS |
| URS-004 | Accuracy check for critical manual receiving data | RSK-003 | MEDIUM | OQ-TC-003 | PASS — OQ-CI-36947244505 | STL-EV-OQ-003-01 | DEV-005 (resolved) | VERIFIED — PASS |
| URS-005 | Corrections preserve prior GxP information | RSK-012 | HIGH | OQ-TC-004, OQ-TC-015 | PASS — OQ-CI-36947244505 | STL-EV-OQ-004-01, STL-EV-OQ-015-01 | None | VERIFIED — PASS |
| URS-006 | Standard users cannot permanently delete completed GxP record | RSK-014 | HIGH | OQ-TC-004 | PASS — OQ-CI-36947244505 | STL-EV-OQ-004-01 | None | VERIFIED — PASS |
| URS-007 | Retrieve by ID/lot and generate accurate complete human-readable and electronic copies | RSK-014 | HIGH | OQ-TC-005, OQ-TC-018 | PASS — OQ-CI-36947244505 | STL-EV-OQ-005-01, STL-EV-OQ-005-02, STL-EV-OQ-018-01 | DEV-007 (resolved) | VERIFIED — PASS |
| URS-008 | Retain relationship among record and associated histories | RSK-014, RSK-012, RSK-013 | HIGH | OQ-TC-005, OQ-TC-018 | PASS — OQ-CI-36947244505 | STL-EV-OQ-005-01, STL-EV-OQ-005-02, STL-EV-OQ-018-01 | None | VERIFIED — PASS |
| URS-009 | Required storage condition | RSK-004 | HIGH | OQ-TC-006 | PASS — OQ-CI-36947244505 | STL-EV-OQ-006-01 | None | VERIFIED — PASS |
| URS-010 | Only compatible configured storage locations | RSK-004 | HIGH | OQ-TC-006 | PASS — OQ-CI-36947244505 | STL-EV-OQ-006-01 | None | VERIFIED — PASS |
| URS-011 | Initial Quarantine status | RSK-005 | HIGH | OQ-TC-007, OQ-TC-018 | PASS — OQ-CI-36947244505 | STL-EV-OQ-007-01, STL-EV-OQ-018-01 | None | VERIFIED — PASS |
| URS-012 | Controlled status values | RSK-005 | HIGH | OQ-TC-007 | PASS — OQ-CI-36947244505 | STL-EV-OQ-007-01 | None | VERIFIED — PASS |
| URS-013 | Enforce permitted status transitions | RSK-005 | HIGH | OQ-TC-008 | PASS — OQ-CI-36947244505 | STL-EV-OQ-008-01 | None | VERIFIED — PASS |
| URS-014 | QA authority required for disposition after hold/review | RSK-005, RSK-008 | HIGH | OQ-TC-008, OQ-TC-011 | PASS — OQ-CI-36947244505 | STL-EV-OQ-008-01, STL-EV-OQ-011-01 | None | VERIFIED — PASS |
| URS-015 | Status change records user/time/prior/new/reason | RSK-005, RSK-015 | HIGH | OQ-TC-008, OQ-TC-015 | PASS — OQ-CI-36947244505 | STL-EV-OQ-008-01, STL-EV-OQ-015-01 | DEV-006 (resolved) | VERIFIED — PASS |
| URS-016 | Identify out-of-range temperature excursion | RSK-006 | HIGH | OQ-TC-009 | PASS — OQ-CI-36947244505 | STL-EV-OQ-009-01 | DEV-001 (resolved); DEV-009 (resolved) | VERIFIED — PASS |
| URS-017 | Correct lower/upper boundary behavior | RSK-006 | HIGH | OQ-TC-009 | PASS — OQ-CI-36947244505 | STL-EV-OQ-009-01 | DEV-001 (resolved); DEV-009 (resolved) | VERIFIED — PASS |
| URS-018 | Excursion record completeness and affected-record linkage | RSK-007 | MEDIUM | OQ-TC-010 | PASS — OQ-CI-36947244505 | STL-EV-OQ-010-01 | None | VERIFIED — PASS |
| URS-019 | Unresolved excursion remains On Hold; Warehouse Operator cannot release | RSK-008 | HIGH | OQ-TC-011, OQ-TC-018 | PASS — OQ-CI-36947244505 | STL-EV-OQ-011-01, STL-EV-OQ-018-01 | None | VERIFIED — PASS |
| URS-020 | QA excursion disposition requires rationale and preserves history | RSK-008 | HIGH | OQ-TC-011, OQ-TC-018 | PASS — OQ-CI-36947244505 | STL-EV-OQ-011-01, STL-EV-OQ-018-01 | None | VERIFIED — PASS |
| URS-021 | Record each custody/responsibility transfer | RSK-009 | LOW | OQ-TC-012 | PASS — OQ-CI-36947244505 | STL-EV-OQ-012-01 | None | VERIFIED — PASS |
| URS-022 | Custody event user/time/prior-new information | RSK-009, RSK-015 | MEDIUM | OQ-TC-012 | PASS — OQ-CI-36947244505 | STL-EV-OQ-012-01 | None | VERIFIED — PASS |
| URS-023 | New custody event does not overwrite prior history | RSK-009 | LOW | OQ-TC-012 | PASS — OQ-CI-36947244505 | STL-EV-OQ-012-01 | None | VERIFIED — PASS |
| URS-024 | Unique active user identity; no shared named-user identity | RSK-010 | HIGH | OQ-TC-013 | PASS — OQ-CI-36947244505 | STL-EV-OQ-013-01 | DEV-004 (resolved) | VERIFIED — PASS |
| URS-025 | Authentication required before GxP access | RSK-010 | HIGH | OQ-TC-001 | PASS — OQ-CI-36947244505 | STL-EV-OQ-001-01 | DEV-004 (resolved); DEV-007, DEV-008 (resolved) | VERIFIED — PASS |
| URS-026 | Functions/data changes restricted by configured role/authority | RSK-010 | HIGH | OQ-TC-013 | PASS — OQ-CI-36947244505 | STL-EV-OQ-013-01 | DEV-004 (resolved) | VERIFIED — PASS |
| URS-027 | Disabled/cancelled account cannot authenticate | RSK-011 | HIGH | OQ-TC-001, OQ-TC-014 | PASS — OQ-CI-36947244505 | STL-EV-OQ-001-01, STL-EV-OQ-014-01 | DEV-004 (resolved) | VERIFIED — PASS |
| URS-028 | Access authorisation creation/change/cancellation is recorded | RSK-011 | HIGH | OQ-TC-014 | PASS — OQ-CI-36947244505 | STL-EV-OQ-014-01 | None | VERIFIED — PASS |
| URS-029 | Audit trail for risk-identified GMP actions | RSK-012 | HIGH | OQ-TC-015 | PASS — OQ-CI-36947244505 | STL-EV-OQ-015-01 | None | VERIFIED — PASS |
| URS-030 | Audit trail contains user/time/record/change/values/reason | RSK-012, RSK-015 | HIGH | OQ-TC-015 | PASS — OQ-CI-36947244505 | STL-EV-OQ-015-01 | None | VERIFIED — PASS |
| URS-031 | Ordinary users cannot alter/delete audit trail; changes do not obscure prior data | RSK-012 | HIGH | OQ-TC-015 | PASS — OQ-CI-36947244505 | STL-EV-OQ-015-01 | None | VERIFIED — PASS |
| URS-032 | QA can retrieve/review intelligible audit trail | RSK-012 | HIGH | OQ-TC-015 | PASS — OQ-CI-36947244505 | STL-EV-OQ-015-01 | DEV-010 (resolved) | VERIFIED — PASS |
| URS-033 | Signature shows/retains signer, date/time, and meaning | RSK-013 | HIGH | OQ-TC-016 | PASS — OQ-CI-36947244505 | STL-EV-OQ-016-01 | None | VERIFIED — PASS |
| URS-034 | Signature permanently linked to record and included in human-readable output | RSK-013 | HIGH | OQ-TC-016, OQ-TC-005 | PASS — OQ-CI-36947244505 | STL-EV-OQ-016-01, STL-EV-OQ-005-01, STL-EV-OQ-005-02 | None | VERIFIED — PASS |
| URS-035 | Signature uses unique user identity and configured credential controls | RSK-013, RSK-010 | HIGH | OQ-TC-017 | PASS — OQ-CI-36947244505 | STL-EV-OQ-017-01 | None | VERIFIED — PASS |

## 4. Coverage checks

### 4.1 Requirement coverage

- URS requirements represented: **35 / 35**
- Requirements without an assigned risk: **0**
- Requirements without planned OQ coverage: **0**

### 4.2 Risk coverage

All 15 risks in STL-RSK-001 have at least one planned OQ path.

High-risk controls are generally covered by V3 tests and, where the control depends on interaction among several functions, by OQ-TC-018 as a second end-to-end path.

### 4.3 Execution status

- Final candidate: `b528234a0a14db68200c9213516d0ed6a76ca56b`
- Execution ID: `OQ-CI-36947244505`
- Frozen OQ result: **18 / 18 PASS**
- URS final status: **35 / 35 VERIFIED — PASS**
- Open validation deviations: **0**

Qualification-apparatus deviations DEV-002 and DEV-003 applied to the execution evidence as a whole and were resolved before the final run. Requirement-specific deviation history remains linked in the table for DEV-001 and DEV-004.

The earlier failed and partially sufficient executions remain historical evidence and are not replaced by this final status.

## 4.4 Supplemental public-release pressure evidence

The final frozen OQ remains the primary qualification path. A separate requirement-derived pressure suite was added before public release after the first bounded qualification had already completed.

Final pressure-suite authority:

- candidate: `b528234a0a14db68200c9213516d0ed6a76ca56b`
- GitHub Actions run: `36897449285`
- development/adversarial tests: **18 / 18 PASS**
- unchanged frozen OQ: **18 / 18 PASS**

Supplemental mappings:

| Requirement(s) | Pressure challenge | Final result | Deviation |
|---|---|---|---|
| URS-004 | Correct critical lot data after QA verification; prior verification must not remain valid | PASS | DEV-005 |
| URS-015 | GMP-relevant On Hold transition without reason | PASS — rejected until reason supplied | DEV-006 |
| URS-007, URS-025 | Regulated record/history/export access without authenticated authority | PASS — unauthenticated access rejected | DEV-007 |
| URS-025 | Same-status status-function call without authentication | PASS — authentication required before no-op return | DEV-008 |
| URS-016, URS-017 | NaN, ±infinity and nonnumeric temperature inputs | PASS — controlled validation rejection | DEV-009 |
| URS-032 | Frozen QA audit-review step executed using QA_REVIEW_01 | PASS | DEV-010 |

These supplemental tests do not redefine the frozen OQ oracle. They close coverage gaps discovered by adversarial review and are preserved as additional evidence.

### 4.4 Supplemental public-release pressure coverage

The final public-release pressure suite supplements the frozen OQ without changing its expected results.

For URS-002, the pressure suite separately verifies that:

- a missing receipt date prevents receiving completion;
- a malformed receipt date is rejected with a controlled validation error;
- a valid receipt date is retained in the authoritative record;
- the receipt date is retained in the electronic copy;
- the receipt date is present in human-readable output.

This supplemental check closed DEV-011 on exact candidate `df40d5b71517e30af425d3b0f02e4e05c920cca6`, run `36947244505`.

## 5. Traceability rules applied during execution

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
| 0.2 | Draft / pre-execution | Pre-OQ source review: URS-007/RSK-014 traceability aligned to human-readable plus electronic record copies. |
| 0.3 | Executed / reconciled | Final run OQ-CI-36947244505 traced across all 35 URS requirements; 18/18 OQ PASS; all recorded validation deviations resolved. |
