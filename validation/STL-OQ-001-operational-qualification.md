# STL-OQ-001 — SampleTrack Lite Operational Qualification Protocol

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Document ID | STL-OQ-001 |
| Title | SampleTrack Lite Operational Qualification Protocol |
| System | SampleTrack Lite |
| Document status | Draft / pre-execution |
| Planned test cases | 18 |
| Test-data authority | STL-OQ-001 Test Configuration and Data Set |
| Approval status | Mock approval: Not executed |

## 1. Purpose

This protocol defines the predeclared Operational Qualification tests for the bounded SampleTrack Lite mock validation scenario.

The protocol is designed from the approved intended use, URS, and functional risk assessment rather than from observed application behavior.

It is intended to provide the primary executed functional-verification evidence for the mock validation package.

This protocol does not constitute production IQ, PQ, supplier qualification, infrastructure qualification, or regulatory approval.

## 2. Governing validation documents

The protocol derives authority from:

- STL-SD-001 — System Description and Intended Use;
- STL-RA-001 — Regulatory Applicability Statement;
- STL-VP-001 — Validation Plan;
- STL-URS-001 — User Requirements Specification;
- STL-RSK-001 — Functional Risk Assessment;
- STL-RTM-001 — Requirements Traceability Matrix;
- STL-OQ-001 Test Configuration and Data Set.

The requirements, risk classifications, configuration, test data, actions, and expected results are to be frozen before decisive execution.

## 3. Current regulatory test-design basis

The protocol incorporates the following source-driven controls:

- risk-based validation and lifecycle traceability;
- parameter-limit, data-limit, and error-handling tests;
- additional accuracy checks for critical manually entered data;
- controlled access and recorded access-authorisation changes;
- system-generated, reviewable GMP audit trails;
- electronic-signature linkage and date/time;
- clear human-readable record copies;
- receiving/storage controls and evidence-based handling of excursions;
- selected 21 CFR Part 11 closed-system and electronic-signature controls as the conditional overlay defined in STL-RA-001.

The exact source mappings remain in STL-URS-001 and STL-RA-001.

## 4. Execution rules

### 4.1 Before execution

The executor shall confirm and record:

- exact system/demonstration-surrogate identity;
- exact OQ protocol revision;
- exact frozen test-configuration artifact;
- user accounts and roles provisioned as specified;
- no real production credentials or regulated data are present;
- test environment is isolated from real GxP operations;
- clock/date display is functioning sufficiently for event comparison;
- evidence-capture method is available.

If a material prerequisite is not met, execution should not be represented as a valid OQ run.

### 4.2 Step results

For each step:

- **PASS** means the observed actual result meets the predeclared expected result;
- **FAIL** means the observed result differs materially from the expected result;
- **NOT EXECUTED** means no qualifying observation was made.

Do not rewrite the expected result after observing a failure.

### 4.3 Test-case result

A test case may be recorded as PASS only when:

- all required steps have a recorded actual result;
- all required steps meet their expected result;
- required evidence is present and attributable;
- no unresolved deviation invalidates the test.

A mismatch requires a deviation or documented invalid-execution disposition before any re-execution.

A later re-test does not overwrite the original failed execution.

### 4.4 Evidence

Evidence should show the decision-relevant behavior rather than every mouse click.

Use stable evidence identifiers:

`STL-EV-OQ-<test>-<sequence>`

Example:

`STL-EV-OQ-009-01`

Evidence may include screenshots, exported records, audit-trail output, structured application output, or other inspectable artifacts.

### 4.5 Execution identity fields

Each test case includes:

- Tester;
- Execution date;
- System/version identity;
- Test record ID(s);
- Case result;
- Deviation ID(s).

Use the actual tester name only for work actually executed.

## 5. Test summary

| Test ID | Focus | Principal URS | Principal risk | Depth |
|---|---|---|---|---|
| OQ-TC-001 | Valid, invalid, and disabled authentication | URS-025, URS-027 | RSK-010, RSK-011 | V3 |
| OQ-TC-002 | Receiving record identity, required fields, creator/time | URS-001–003 | RSK-001, RSK-002, RSK-015 | V2 |
| OQ-TC-003 | Critical manual-data accuracy check | URS-004 | RSK-003 | V2 |
| OQ-TC-004 | Correction history and deletion prevention | URS-005, URS-006 | RSK-012, RSK-014 | V3 |
| OQ-TC-005 | Record retrieval, related history, human-readable copy | URS-007, URS-008 | RSK-014 | V3 |
| OQ-TC-006 | Storage condition/location compatibility | URS-009, URS-010 | RSK-004 | V3 |
| OQ-TC-007 | Initial and controlled material statuses | URS-011, URS-012 | RSK-005 | V2 |
| OQ-TC-008 | Status sequencing, QA authority, rationale | URS-013–015 | RSK-005, RSK-015 | V3 |
| OQ-TC-009 | Temperature lower/upper boundary behavior | URS-016, URS-017 | RSK-006 | V3 |
| OQ-TC-010 | Excursion-record completeness and linkage | URS-018 | RSK-007 | V2 |
| OQ-TC-011 | Excursion hold enforcement and QA disposition | URS-019, URS-020 | RSK-008 | V3 |
| OQ-TC-012 | Chain-of-custody history | URS-021–023 | RSK-009, RSK-015 | V1/V2 |
| OQ-TC-013 | Unique identity and role-based authorization | URS-024, URS-026 | RSK-010 | V3 |
| OQ-TC-014 | Access-authorisation lifecycle record | URS-027, URS-028 | RSK-011 | V3 |
| OQ-TC-015 | Audit-trail coverage, content, immutability, reviewability | URS-005, URS-029–032 | RSK-012, RSK-015 | V3 |
| OQ-TC-016 | E-signature manifestation and record linkage | URS-033, URS-034 | RSK-013 | V3 |
| OQ-TC-017 | E-signature identity and negative authentication challenge | URS-035 | RSK-013, RSK-010 | V3 |
| OQ-TC-018 | End-to-end regulated workflow | Cross-cutting | RSK-004–006, RSK-008, RSK-010, RSK-012–014 | V3 |

---

# 6. Detailed test cases

## OQ-TC-001 — Valid, invalid, and disabled authentication

**Objective:** Verify that GxP functions require successful authentication and that invalid or disabled credentials do not establish an authenticated session.

**Requirements:** URS-025, URS-027  
**Risks:** RSK-010, RSK-011  
**Preconditions:** WH_OP_01 active; WH_DISABLED_01 disabled.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | Attempt to access a GxP data-changing function without authentication. | Access is denied or the user is routed to authentication; no GxP change can be made. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | Authenticate as WH_OP_01 with valid locally provisioned credentials. | Authentication succeeds and a Warehouse Operator session is established. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | Log out and attempt authentication as WH_OP_01 using an incorrect password. | Authentication fails and no authenticated session is established. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | Attempt authentication as WH_DISABLED_01 using its otherwise valid locally provisioned credentials. | Authentication is rejected because the account is disabled. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Attempt a GxP data-changing function after each failed authentication. | No unauthorized GxP operation is permitted. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** login/access results sufficient to distinguish valid, invalid, and disabled paths.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** N/A  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-002 — Receiving record identity, required fields, creator, and time

**Objective:** Verify required receiving data, unique/persistent record identity, and attributable creation metadata.

**Requirements:** URS-001, URS-002, URS-003  
**Risks:** RSK-001, RSK-002, RSK-015  
**Preconditions:** WH_OP_01 authenticated; primary receiving fixture available.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | Start a new DEMO-RX-COLD-001 receiving record and omit the lot/batch number. Attempt completion. | Completion is blocked and the missing required field is identified. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | Enter all required receiving fields from the frozen fixture and complete the record. | Record completes successfully. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | Inspect the generated SampleTrack record identifier. | A non-empty unique record ID is assigned. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | Retrieve/reopen the same record. | The same persistent record ID is retained. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Inspect creation attribution. | WH_OP_01 and the creation date/time are recorded for the completed record. | NOT EXECUTED | TBD | NOT EXECUTED |
| 6 | Create a second valid record using LOT-OQ-002. | The second record receives a different unique SampleTrack record ID. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** completed record, generated IDs, creator/time metadata, required-field rejection.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-003 — Critical manual-data accuracy check

**Objective:** Verify that critical manually entered receiving data cannot support release without the configured independent/electronic accuracy check.

**Requirement:** URS-004  
**Risk:** RSK-003  
**Preconditions:** Dedicated Quarantine record created by WH_OP_01; QA_REVIEW_01 active.

Critical fields:

- product/material identifier;
- lot/batch number;
- required storage condition.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | From a Quarantine record with no completed critical-data verification, attempt the configured release path. | Release is blocked because critical-data verification is incomplete. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | As QA_REVIEW_01, perform the configured critical-data verification using matching product, lot, and storage-condition values. | Verification completes and is attributable to QA_REVIEW_01 and the record. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | Confirm the record now indicates that critical-data verification is complete. | Verification state is visible/retained for the record. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | On a second Quarantine record, perform the verification with a deliberately discrepant critical value. | Verification does not complete as successful; the discrepancy is identified or the release prerequisite remains unsatisfied. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Attempt release of the discrepant/unverified record. | Release remains blocked. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** unverified release block, successful verification attribution, discrepant verification behavior.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-004 — Correction history and deletion prevention

**Objective:** Verify that permitted GxP corrections preserve prior information and that ordinary business users cannot permanently delete completed GxP records.

**Requirements:** URS-005, URS-006  
**Risks:** RSK-012, RSK-014  
**Preconditions:** Completed test receiving record exists.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | As an authorized user, perform a permitted correction to a GxP field and provide the configured reason for change. | Correction is accepted only through the permitted path and current value is updated. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | Inspect record history/audit information for the correction. | Prior value remains recoverable and the change is associated with acting user, date/time, new value, and required reason. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | As WH_OP_01, attempt to permanently delete the completed GxP record. | Permanent deletion is denied. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | As QA_REVIEW_01, attempt to permanently delete the completed GxP record through ordinary application functions. | Permanent deletion is denied. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Retrieve the record again. | Record and its retained correction history remain available. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** before/after record values, change reason/history, deletion denial, retained record.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-005 — Record retrieval, related history, and human-readable copy

**Objective:** Verify reliable retrieval and an accurate, complete human-readable representation of the regulated record and related history available at the time of export.

**Requirements:** URS-007, URS-008  
**Risk:** RSK-014  
**Preconditions:** A record exists with receiving, location/status, and at least one history event.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | Retrieve the record by its unique SampleTrack record ID. | Correct record is returned. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | Retrieve the same record by lot/batch number. | Same record is returned without ambiguity. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | Review the record's associated receiving, status/location, and available history relationships. | Related in-scope information remains associated with the same record identity. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | Generate the configured human-readable record copy/export. | A clear human-readable copy is produced. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Compare the human-readable output with the authoritative application record for the fields/history in scope. | Output is accurate and complete for the tested regulated content; no tested field changes meaning during output. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** application record plus exported/human-readable output and comparison.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-006 — Required storage condition and compatible location assignment

**Objective:** Verify that storage assignment respects configured storage conditions and active-location compatibility.

**Requirements:** URS-009, URS-010  
**Risk:** RSK-004  
**Preconditions:** DEMO-RX-COLD-001 record in controllable state; REFR-A1, REFR-A2, CRT-A1, RETIRED-R1 configured.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | Confirm DEMO-RX-COLD-001 requires REFRIGERATED_2_8C. | Required condition is present on the active record. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | Assign REFR-A1. | Assignment succeeds because REFR-A1 is active and compatible. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | Attempt assignment to CRT-A1. | Assignment is rejected because the location is incompatible with REFRIGERATED_2_8C. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | Attempt assignment to RETIRED-R1. | Assignment is rejected because the location is inactive. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Assign REFR-A2. | Assignment succeeds and current location is updated to REFR-A2 with appropriate history. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** compatible/incompatible/inactive assignment results and resulting record state/history.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-007 — Initial and controlled material statuses

**Objective:** Verify configured initial status and controlled status vocabulary.

**Requirements:** URS-011, URS-012  
**Risk:** RSK-005  
**Preconditions:** WH_OP_01 authenticated.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | Complete a valid new receiving record. | Initial status is automatically set to Quarantine. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | Inspect available configured material-status values through an authorized status function. | Configured values include Quarantine, Released, On Hold, Rejected, Returned, and Recalled. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | Attempt to enter or select an unconfigured free-text status such as "AVAILABLE-NOW". | Unconfigured status is not accepted as the material's controlled status. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | Reopen the record. | Controlled status remains the last valid configured status. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** initial record state and controlled/unconfigured status behavior.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-008 — Status sequencing, QA authority, and rationale

**Objective:** Verify permitted sequencing and authority for material disposition.

**Requirements:** URS-013, URS-014, URS-015  
**Risks:** RSK-005, RSK-015  
**Preconditions:** Quarantine record with critical-data verification complete; WH_OP_01 and QA_REVIEW_01 active.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | As WH_OP_01, attempt Quarantine → Released. | Transition is denied because Warehouse Operator lacks QA disposition authority. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | As QA_REVIEW_01, attempt the configured release action without required rationale/signature completion. | Release does not complete until all configured QA disposition prerequisites are satisfied. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | As QA_REVIEW_01, enter a valid rationale and complete the required QA release signature. | Quarantine → Released succeeds. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | Inspect status history. | History identifies prior status, new status, QA_REVIEW_01, date/time, and disposition rationale. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Attempt a configured prohibited sequence that bypasses required review. | Prohibited sequence is rejected and the current valid status is retained. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** denied Warehouse transition, successful QA transition, rationale, signature reference, status history.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-009 — Temperature excursion lower/upper boundary values

**Objective:** Verify exact inclusive threshold behavior for the frozen REFRIGERATED_2_8C configuration.

**Requirements:** URS-016, URS-017  
**Risk:** RSK-006  
**Preconditions:** Dedicated DEMO-RX-COLD-001 records or resettable test context.

The expected classification is fixed before execution:

| Step | Input | Expected result | Actual result | Evidence | Step result |
|---:|---:|---|---|---|---|
| 1 | 1.9 °C | Classified as excursion; affected record follows configured excursion/hold behavior. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | 2.0 °C | Classified within range; no excursion solely due to this value. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | 2.1 °C | Classified within range. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | 7.9 °C | Classified within range. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | 8.0 °C | Classified within range; no excursion solely due to this value. | NOT EXECUTED | TBD | NOT EXECUTED |
| 6 | 8.1 °C | Classified as excursion; affected record follows configured excursion/hold behavior. | NOT EXECUTED | TBD | NOT EXECUTED |

**Acceptance:** All six predeclared values must produce the expected classification. Any boundary mismatch is a material failure requiring deviation assessment.

**Planned evidence:** exact input and resulting classification/state for all six values.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-010 — Excursion-record completeness and record linkage

**Objective:** Verify required excursion information and unambiguous association with affected material.

**Requirement:** URS-018  
**Risk:** RSK-007  
**Preconditions:** DEMO-RX-COLD-001 test record exists.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | Start a new excursion record and omit a required field such as event date/time or source/reporter. Attempt completion. | Incomplete excursion record cannot be completed as a valid event. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | Complete an excursion using a frozen out-of-range value and all required fields. | Excursion event is saved successfully. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | Retrieve the affected inventory record. | Excursion is associated with the correct SampleTrack record. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | Inspect the excursion record. | It retains the affected record, observed condition/temperature, event date/time, source/reporter, and configured available duration/details. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Search/retrieve the excursion again from the affected record. | Same excursion identity and content are returned. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** incomplete-event rejection plus completed linked excursion record.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-011 — Excursion hold enforcement and QA disposition

**Objective:** Verify that unresolved excursion material remains restricted and only authorized QA disposition can resolve the hold.

**Requirements:** URS-019, URS-020  
**Risk:** RSK-008  
**Preconditions:** Released DEMO-RX-COLD-001 record; WH_OP_01 and QA_REVIEW_01 active.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | Record a confirmed 8.1 °C excursion against the Released record. | The record is placed/maintained On Hold according to the configured excursion rule. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | As WH_OP_01, attempt On Hold → Released. | Transition is denied. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | As QA_REVIEW_01, attempt disposition without required rationale. | Disposition does not complete. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | As QA_REVIEW_01, enter a mock technical disposition rationale and complete the configured QA signature for release or rejection. | Authorized disposition completes to the selected permitted terminal status. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Inspect excursion/disposition history. | History retains the excursion, hold state, QA identity, date/time, rationale, resulting status, and signature relationship. | NOT EXECUTED | TBD | NOT EXECUTED |

**Important boundary:** The mock rationale is only a workflow test input. This OQ does not scientifically determine whether a real drug exposed to an excursion is acceptable.

**Planned evidence:** excursion event, On Hold state, denied Warehouse release, completed QA disposition/history.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-012 — Chain-of-custody sequence and retained history

**Objective:** Verify attributable, append-style custody history.

**Requirements:** URS-021, URS-022, URS-023  
**Risks:** RSK-009, RSK-015  
**Preconditions:** Active test record assigned to REFR-A1.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | As WH_OP_01, record a custody/location event from receiving control to REFR-A1. | Event is recorded against the correct SampleTrack record with WH_OP_01 and date/time. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | As WH_OP_02, record a second permitted custody event or transfer to REFR-A2. | Second event is recorded with WH_OP_02 and relevant prior/new information. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | Retrieve custody history. | Both events remain present in chronological history. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | Inspect the current record. | Current state reflects the latest valid event without overwriting prior custody history. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** two custody events and retained chronological history.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-013 — Unique user identity and role-based authorization challenge

**Objective:** Verify uniqueness of named user identity and separation of Warehouse, QA, and Administrator authority.

**Requirements:** URS-024, URS-026  
**Risk:** RSK-010  
**Preconditions:** SYS_ADMIN_01 active; WH_OP_01 and QA_REVIEW_01 active.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | As SYS_ADMIN_01, attempt to create/assign a second active named user using an already assigned unique user ID. | Duplicate active user identity is rejected or otherwise prevented. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | As WH_OP_01, attempt a QA-only disposition action. | Action is denied. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | As WH_OP_01, attempt a user/role-administration action. | Action is denied. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | As QA_REVIEW_01, attempt a user/role-administration action. | Action is denied. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | As SYS_ADMIN_01, attempt a QA-only disposition/signature solely by virtue of administrator role. | QA disposition/signature authority is denied unless separately and explicitly assigned; the frozen scenario does not assign it. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** duplicate-identity behavior and cross-role denial results.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-014 — Access-authorisation creation/change/cancellation records

**Objective:** Verify that user-access lifecycle changes are recorded and that cancellation is effective.

**Requirements:** URS-027, URS-028  
**Risk:** RSK-011  
**Preconditions:** SYS_ADMIN_01 authenticated; disposable mock user ID available.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | As SYS_ADMIN_01, create a new mock Warehouse Operator access authorization. | User/access authorization is created and the event is recorded with sufficient identity/time information. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | Change the user's permitted role/authorization within the test scenario. | Change succeeds only through administration function and the change is recorded. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | Inspect access-authorisation history. | Creation/change record identifies what authorization changed and when; acting administrator is attributable where supported by the configured model. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | Disable/cancel the user's access. | Account becomes disabled/cancelled and the cancellation is recorded. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Attempt authentication using the disabled/cancelled account. | Authentication is rejected. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** access lifecycle history and disabled-login result.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** N/A / access object ID TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-015 — Audit-trail coverage, content, immutability, and reviewability

**Objective:** Verify that risk-identified GMP events create usable audit evidence and that ordinary users cannot alter/delete the audit trail.

**Requirements:** URS-005, URS-029, URS-030, URS-031, URS-032  
**Risks:** RSK-012, RSK-015  
**Preconditions:** A test record is available for controlled create/change/status/disposition activity.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | Create a receiving record and perform one permitted GMP-relevant correction with reason. | Audit/history contains creation and correction events. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | Perform a material-status change through the configured QA workflow. | Status-change event is represented in audit/history. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | Record an excursion and QA disposition/signature event. | Excursion/disposition/signature events are represented as required by the configured audit model. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | Inspect representative change-event detail. | Acting user, date/time, affected record/action, prior/new values where applicable, and required reason are intelligible. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | As WH_OP_01, attempt to edit or delete an audit-trail entry through ordinary application functions. | Audit entry cannot be altered or deleted. | NOT EXECUTED | TBD | NOT EXECUTED |
| 6 | As QA_REVIEW_01, retrieve the audit trail associated with the record. | Audit information is available and convertible/displayed in a generally intelligible form. | NOT EXECUTED | TBD | NOT EXECUTED |
| 7 | Compare the audit events with the known test actions. | The tested event sequence is attributable and no tested prior value is obscured by the later change. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** audit-trail display/export for representative events, failed alteration attempt, comparison to test actions.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-016 — Electronic-signature manifestation and permanent record linkage

**Objective:** Verify QA electronic-signature content, linkage, and inclusion in human-readable output.

**Requirements:** URS-033, URS-034  
**Risk:** RSK-013  
**Preconditions:** QA_REVIEW_01 authenticated; record ready for a configured QA signed action.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | Complete the configured QA signed action using QA_REVIEW_01 and correct locally provisioned signature credentials. | Signature completes and the business action is associated with the signed record/action. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | Inspect the electronic-signature manifestation. | Signer's displayed name, date/time, and meaning of the signature are present. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | Retrieve/reopen the signed record. | Signature remains linked to the same record/action. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | Generate the human-readable copy/output for the signed record. | Signature manifestation is included with the human-readable record output. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Attempt, through ordinary application means, to transfer/copy the existing signature to a different record without executing a new signature. | Existing signature cannot be excised/copied/transferred as a valid signature on another record by ordinary means. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** signed record, signature manifestation, human-readable output, negative transfer/copy behavior.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-017 — Electronic-signature identity and negative authentication challenge

**Objective:** Verify that the configured non-biometric QA signature uses the unique authenticated identity and cannot ordinarily be applied with incorrect credentials or by another role.

**Requirement:** URS-035  
**Risks:** RSK-013, RSK-010  
**Preconditions:** QA_REVIEW_01 and WH_OP_01 active; record ready for QA signed action.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | As QA_REVIEW_01, initiate the signed action and enter an incorrect password/re-authentication component. | Signature is rejected and signed action does not complete. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | Confirm the record after the failed signature attempt. | No valid QA signature is recorded for the failed attempt and the protected disposition is not completed. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | As WH_OP_01, attempt the QA signed action. | Warehouse Operator cannot apply the QA signature/action. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | As QA_REVIEW_01, execute the action using the correct unique identity and configured password control. | Signature/action succeeds. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Inspect the resulting signature attribution. | Signature is attributed to QA_REVIEW_01, not another user. | NOT EXECUTED | TBD | NOT EXECUTED |

**Planned evidence:** failed incorrect-credential attempt, denied Warehouse attempt, successful QA signature and attribution.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

## OQ-TC-018 — End-to-end regulated workflow

**Objective:** Verify the principal control chain across multiple system functions using one traceable record.

**Requirements:** Cross-cutting confirmation of the risk-critical workflow  
**Risks:** RSK-004, RSK-005, RSK-006, RSK-008, RSK-010, RSK-012, RSK-013, RSK-014  
**Preconditions:** Frozen configuration active; WH_OP_01 and QA_REVIEW_01 active; dedicated LOT-OQ-004.

| Step | Action | Expected result | Actual result | Evidence | Step result |
|---:|---|---|---|---|---|
| 1 | As WH_OP_01, create a complete DEMO-RX-COLD-001 receiving record using LOT-OQ-004. | Unique record created in Quarantine with creator/time attribution. | NOT EXECUTED | TBD | NOT EXECUTED |
| 2 | As QA_REVIEW_01, complete critical-data verification. | Verification completes and remains attributable to QA_REVIEW_01. | NOT EXECUTED | TBD | NOT EXECUTED |
| 3 | Assign the record to REFR-A1 and perform the configured QA release with rationale/signature. | Compatible location is accepted; valid QA release results in Released status with attributable history/signature. | NOT EXECUTED | TBD | NOT EXECUTED |
| 4 | Record a custody transfer/location event permitted by the workflow. | Custody event is appended without loss of prior history. | NOT EXECUTED | TBD | NOT EXECUTED |
| 5 | Enter a temperature of 8.1 °C as an excursion condition against the record. | Event is classified as excursion and material becomes/remains On Hold. | NOT EXECUTED | TBD | NOT EXECUTED |
| 6 | As WH_OP_01, attempt to return the material to Released. | Attempt is denied. | NOT EXECUTED | TBD | NOT EXECUTED |
| 7 | As QA_REVIEW_01, enter the mock technical disposition rationale and execute the configured signed disposition. | Authorized disposition completes to the selected permitted status. | NOT EXECUTED | TBD | NOT EXECUTED |
| 8 | Retrieve the final record, related histories, audit trail, and signature information. | Receiving, status, location/custody, excursion, QA disposition, audit, and signature information remain linked to the same record and are intelligible. | NOT EXECUTED | TBD | NOT EXECUTED |
| 9 | Generate a human-readable record output. | Output accurately represents the tested regulated record and includes applicable signature information. | NOT EXECUTED | TBD | NOT EXECUTED |
| 10 | Compare the final history with the known execution sequence. | The complete tested sequence is reconstructable and no material failed/blocked action has been misrepresented as a successful disposition. | NOT EXECUTED | TBD | NOT EXECUTED |

**Important boundary:** The end-to-end scenario verifies configured workflow behavior. It does not establish scientific suitability of a real temperature-exposed product or a formal PQ under production conditions.

**Planned evidence:** one coherent record bundle linking the complete test sequence.

**Tester:** TBD  
**Execution date:** TBD  
**System/version:** TBD  
**Test record(s):** TBD  
**Case result:** NOT EXECUTED  
**Deviation(s):** TBD

---

# 7. Protocol-level acceptance criteria

The OQ protocol reaches a positive execution disposition only if:

1. all 18 test cases are executed or formally dispositioned;
2. all High-risk V3 control paths have valid evidence;
3. OQ-TC-009 passes all six frozen temperature-boundary inputs;
4. unauthorized release/disposition paths are demonstrably blocked;
5. unresolved excursion material cannot be released by Warehouse Operator;
6. access restrictions and disabled-account behavior meet expected results;
7. audit-trail evidence is present, attributable, non-obscuring, protected from ordinary alteration, and reviewable for the tested events;
8. required electronic-signature manifestation and linkage behave as expected;
9. required records can be retrieved and represented accurately in human-readable form;
10. material deviations are assessed and any required re-execution is completed without erasing the original result;
11. the system/configuration identity under test remains identifiable.

A high raw pass count does not compensate for a failed release-critical control.

# 8. Conditions requiring deviation before continuation

Open a validation deviation when, for example:

- expected and actual behavior materially differ;
- a prerequisite was not satisfied but execution proceeded;
- the wrong user/role, product fixture, storage limit, or configuration was used;
- evidence required to interpret the result is missing or unusable;
- system identity changed during execution;
- the protocol itself contains an error that affects interpretation;
- an unplanned system/configuration change is required to continue.

Routine note-taking corrections that do not affect evidentiary meaning do not need to be inflated into formal deviations.

# 9. Re-test rule

For a failed/deviated case:

1. preserve the original execution and evidence;
2. identify the deviation and impact;
3. establish whether the defect lies in the system/configuration, protocol, evidence procedure, or environment;
4. make only the controlled correction justified by that assessment;
5. determine which test cases are affected;
6. re-execute under a new execution identity;
7. link both original and re-test evidence in the RTM and deviation record.

Do not replace the failed result with the later result.

# 10. Execution record summary

To be completed only after execution.

| Test | Initial result | Deviation | Re-test result | Final test disposition |
|---|---|---|---|---|
| OQ-TC-001 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-002 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-003 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-004 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-005 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-006 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-007 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-008 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-009 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-010 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-011 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-012 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-013 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-014 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-015 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-016 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-017 | NOT EXECUTED | TBD | TBD | OPEN |
| OQ-TC-018 | NOT EXECUTED | TBD | TBD | OPEN |

# 11. References

- Health Canada GUI-0050 — Annex 11 to the good manufacturing practices guide: Computerized Systems  
  https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/annex-11-guide-computerized-systems-gui-0050.html
- Health Canada GUI-0069 — Guidelines for environmental control of drugs during storage and transportation  
  https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/guidelines-temperature-control-drug-products-storage-transportation-0069.html
- FDA — Part 11, Electronic Records; Electronic Signatures — Scope and Application  
  https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application
- eCFR — 21 CFR Part 11  
  https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11
- ISPE GAMP 5 Second Edition — industry guidance; copyrighted guide text is not reproduced here.

# 12. Revision history

| Revision | Status | Description |
|---|---|---|
| 0.1 | Draft / pre-execution | Initial 18-case risk-based OQ protocol with predeclared expected results. |
