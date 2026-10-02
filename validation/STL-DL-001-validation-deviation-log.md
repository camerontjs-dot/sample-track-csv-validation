# STL-DL-001 — SampleTrack Lite Validation Deviation Log

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Document ID | STL-DL-001 |
| System | SampleTrack Lite demonstration surrogate |
| Status | Closed for successor candidate `df40d5b71517e30af425d3b0f02e4e05c920cca6` |
| Approval status | Mock approval: Not executed |

## DEV-001 — Upper temperature boundary classified as excursion

**Training seed:** Yes. This is the planned seeded system/configuration defect.

**Observed execution:** `OQ-EXEC-001`  
**GitHub Actions run:** `36812149305`  
**Candidate:** `e1636c513661a8d6784e9594f8929b1592b690c7`  
**Affected test:** `OQ-TC-009`  
**Affected requirements:** `URS-016`, `URS-017`  
**Affected risk:** `RSK-006` — HIGH  
**Initial OQ summary:** 17 PASS / 1 FAIL

### Observation

The frozen `REFRIGERATED_2_8C` test oracle defines the upper limit as **8.0 °C inclusive**.

Observed boundary results:

| Input | Expected | Actual | Result |
|---:|---|---|---|
| 1.9 °C | Excursion | Excursion | PASS |
| 2.0 °C | Within range | Within range | PASS |
| 2.1 °C | Within range | Within range | PASS |
| 7.9 °C | Within range | Within range | PASS |
| 8.0 °C | Within range | Excursion | **FAIL** |
| 8.1 °C | Excursion | Excursion | PASS |

At 8.0 °C the surrogate also created an excursion record and placed the affected test material On Hold.

### Failure classification

**SYSTEM / CONFIGURATION FAILURE**

The frozen protocol and fixture agree that 8.0 °C is within range. Neighboring boundary cases behaved consistently with the frozen oracle except the inclusive upper boundary.

The initial implementation uses an exclusive upper-bound comparison for excursion classification.

### Impact assessment

This is a material validation failure because:

- the defect directly affects `RSK-006`, a High risk;
- a valid in-range condition is incorrectly represented as an excursion;
- the defect causes an unnecessary On Hold state and quality workflow;
- the same comparison path is used by end-to-end excursion handling.

The observed direction is conservative with respect to product exposure because it creates a false-positive excursion rather than failing to detect 8.1 °C. It is still unacceptable for the specified intended behavior and would create inaccurate regulated records and unnecessary quality disposition activity.

### Prior evidence impact

- `OQ-TC-009`: **FAILED** and must be re-executed after correction.
- `OQ-TC-018`: initial execution used 8.1 °C and passed. Because the correction changes the same temperature comparison function, re-execute `OQ-TC-018` or the full OQ to demonstrate no regression in the end-to-end path.
- Other initial cases remain informative but do not close their final RTM status until the corrected candidate is qualified.

### Required correction

Change the upper excursion comparison from:

`temperature >= upper_limit`

to:

`temperature > upper_limit`

No change is authorized to the frozen 8.0 °C expected result.

### Re-test requirement

Run the complete frozen OQ against the corrected candidate. Full re-execution is selected because the automated qualification cost is low and provides stronger regression evidence than a partial rerun.

### Status

`RESOLVED — CORRECTED / FULL RETEST PASS`

### Correction and retest receipt

The authorized comparison correction was applied without changing the frozen expected result.

Corrected candidate: `7a8f114bfd67935d8354e922873fa54f0a2c37c9`  
Candidate tree: `07182c62c251f767ccfde481816d5f22a84daecc`  
GitHub Actions run: `36812375284`  
Job: `110210033595`  
Development tests: **8 / 8 PASS**  
Frozen OQ: **18 / 18 PASS**  
Corrected `sampletrack.py` SHA-256: `96c033656393a8a7f8896dfe9ac8cd868895f4aae8ce52999ea20f41d6ae3ddb`  
OQ runner SHA-256: `9e11e8474bc97bc6b5c9fe8f6ae461cce82b07047486dda2937db6ee0dd53c1b`  
Retest artifact: `11139822400`  
Artifact digest: `sha256:95739a76b983693e2d438ee1eecbc7584fdbf2aba16b2d7e9cfc08ea76d45d78`

All six frozen boundary values passed on the corrected candidate, including **8.0 °C → Within range** and **8.1 °C → Excursion**.

DEV-001 is behaviorally resolved. Final package closure still depends on resolving the separate evidence-identification deficiency recorded as DEV-003.

The original run and evidence must remain preserved after correction.

### Secondary local preservation receipt — original `fed1f956…` candidate

A separate local recovery/qualification review later inspected the earlier candidate:

`fed1f956a8b6f251300599838a5b2ad88783d298`

and preserved the existing first-run output without rerunning or repairing it.

Observed from the preserved bundle:

- OQ summary: **17 PASS / 1 FAIL**;
- failing case: `OQ-TC-009`;
- failing step: frozen **8.0 °C** input;
- expected: `Within range`;
- actual: `Excursion`;
- classification: **system / configuration failure**;
- preserved artifacts: **22**;
- manifest entries verified: **21 / 21**;
- receipt SHA-256: `1e90f8eb0edb670faef4fdf33877a6cddae652faf50ab2962d07beb44d1aa51e`;
- local preservation branch: `qualification/preserve-fed1f-first-run-20261001`;
- no source/protocol correction, commit, push, merge, or promotion was performed by that review.

Local receipt path at time of review:

`/private/tmp/csv-demo-qual-recovery-fed1f.fB1CAa/qualification/fed1f-first-run-preserved/qualification-receipt.json`

Important limitation: the recovery environment (macOS 27.0 / 26A428, arm64, Python 3.14.4, SQLite 3.53.4) is **not** historical execution attestation. The original compile/unit-test results, original execution environment, invocation trace, and captured process exit code remain unknown. A runner-contract exit of 1 is inferred from the preserved 17/1 result, not directly observed.

GitHub lineage review found that `fed1f956…` is an ancestor of the later hosted DEV-001 candidate `e1636c513661a8d6784e9594f8929b1592b690c7`. Between those commits, GitHub records only qualification-workflow / candidate-metadata additions. The application and OQ-runner blobs are byte-identical:

- `demo/sampletrack.py`: `4fbe45cc3c5314c8456d390f6da581db9e087e19`
- `demo/oq_runner.py`: `aa98aae1dc503c964136447e94e7b83f9878073e`

Accordingly, this local receipt is treated as **corroborating preservation evidence for the same pre-correction upper-bound defect state**, not as a new OQ execution and not as historical environment evidence.

It does not change the final DEV-001 resolution on the corrected candidate.





## DEV-004 — Authentication boundary does not provide controlled denial

**Discovered during:** corrected protocol-conformance execution `OQ-CI-36813093395`  
**Candidate:** `9dfe0aa25ecd86173fc654b90665d51455ebb156`  
**Affected test:** `OQ-TC-001`  
**Affected requirements:** `URS-024`, `URS-025`, `URS-026`, `URS-027`  
**Affected risks:** `RSK-010`, `RSK-011`

### Observation

After DEV-002 corrected the OQ harness to execute the frozen unauthenticated-access steps, `OQ-TC-001` failed.

Three unauthenticated GxP-write challenges produced:

`AttributeError: 'NoneType' object has no attribute 'role'`

instead of a controlled authentication/access denial.

The run result was **17 PASS / 1 FAIL**.

### Classification

**SYSTEM AUTHENTICATION / AUTHORIZATION BOUNDARY FAILURE**

The qualification harness used the frozen expected behavior: a GxP data-changing function must require authenticated access and reject an unauthenticated attempt.

### Additional code-inspection finding

The current `Session` object is directly caller-constructible and `_require_role` trusts its role field without checking that the application actually issued the session.

This creates a plausible forged-session authorization path.

This exposure was subsequently **confirmed by a requirement-derived adversarial test** before implementation repair.

### Impact assessment

The observed uncontrolled exception is a validation failure for the authentication boundary.

If the forged-session path is executable, the impact is more severe because an unauthenticated caller could potentially construct an apparently authorized Warehouse or QA session and bypass the intended authentication gate.

Final validation disposition is blocked until this boundary is corrected and requalified.

### Pre-correction adversarial test

Before implementation repair, add development tests derived from the authentication requirement that require:

1. an unauthenticated GxP write to raise a controlled `AuthenticationError`;
2. a caller-constructed forged Warehouse session to be rejected with `AuthenticationError`.

Preserve the first test result.

### Planned correction

If the adversarial test confirms the exposure:

- issue opaque session tokens only after successful authentication;
- validate each session token and its user/role against application-owned state before protected operations;
- reject absent, forged, expired, disabled-user, or role-stale sessions with controlled authentication errors;
- invalidate existing sessions when access is disabled or role authorization changes.

### Status

`RESOLVED — AUTHORITY CORRECTED / ADVERSARIAL TEST PASS / FULL OQ PASS`

### Pre-correction adversarial receipt

Candidate: `5a77e66e0bb165fb040c33e9445925b3e9eb070d`  
Candidate tree: `0c90945319a2304d90394aae94ac0d3b65147967`  
GitHub Actions run: `36813247201`  
Job: `110212683378`

Development gate result: **10 tests, 1 failure, 1 error**.

Observed:

- unauthenticated GxP write raised uncontrolled `AttributeError`, not `AuthenticationError`;
- a caller-constructed Warehouse `Session` did **not** raise `AuthenticationError` and successfully passed the application role gate.

The forged-session bypass is therefore OBSERVED, not merely inferred.

### Authorized implementation correction

The system now:

- issues an opaque random token only after successful authentication;
- stores issued session authority in application-owned state;
- validates token, user identity, role, active status, and current role before protected operations;
- rejects absent, forged, expired, disabled-user, or stale-role sessions with controlled authentication failure;
- invalidates a user's existing sessions when the account is disabled or role authorization changes.

The frozen OQ expected results remain unchanged.

### Final corrective qualification receipt

Corrected candidate: `37a23e1bb28c4fc96d6fcdc252d91e8a4e57ba0e`  
Candidate tree: `0fd797f7a4532ef18284aa8484c2db7036532c02`  
GitHub Actions run: `36813357212`  
Job: `110213023142`  
Development tests: **10 / 10 PASS**  
Frozen OQ: **18 / 18 PASS**  
`sampletrack.py` SHA-256: `c0bcf3919279d41aabe90f63056f8b63b57e38f3ca8a3d146ab5a128ea28afe4`  
OQ runner SHA-256: `0789c67da040a73904602b3ef0638e3ed27adca72268c180b92ffdf207ce68af`  
Artifact: `11140757299`  
Artifact digest: `sha256:94f82fb01bdd9999c4d71ccbd2587702181ab45bf7833dc39cb987b16051a490`

The final execution explicitly passed:

- unauthenticated GxP access denial;
- invalid-password post-failure GxP access denial;
- disabled-account post-failure GxP access denial;
- forged-session development challenge;
- all role/authority OQ paths.

DEV-004 is resolved for the exact qualified candidate. The original pre-correction failures remain preserved.

## DEV-002 — Automated OQ harness did not preserve frozen protocol step coverage

**Training seed category:** Protocol / execution discrepancy.

### Observation

After the first successful behavioral retests, a qualification-apparatus review compared the frozen `STL-OQ-001` steps against the automated `demo/oq_runner.py` implementation.

The review found that several runner cases grouped multiple protocol steps under one assertion, and at least one material frozen requirement was not directly exercised:

- `OQ-TC-001` did not attempt a GxP data-changing function without an authenticated session and did not directly challenge a data-changing function after failed authentication.
- Other cases combined protocol actions and verification into fewer assertions, reducing step-level inspectability.
- `OQ-TC-017` did not separately confirm the absence of a signature after a failed credential attempt.

### Classification

**PROTOCOL / EXECUTION APPARATUS DISCREPANCY**

The frozen protocol itself remains unchanged. The gap is between that protocol and the automated qualification harness.

### Impact assessment

The prior case-level 18/18 results remain useful observations of the behavior that was actually exercised.

They are not sufficient, by themselves, to claim complete execution of every frozen OQ step.

Final RTM closure and VSR eligibility are therefore held pending a protocol-conformance correction and full OQ re-execution.

### Root cause

The first runner implementation was designed around case-level behavior and evidence bundles rather than an explicit protocol-step-to-runner conformance check.

### Correction

Without changing any frozen expected result:

1. map every frozen protocol step to an explicit runner assertion or clearly expanded loop case;
2. add direct unauthenticated GxP access challenges;
3. add explicit verification that failed electronic-signature authentication leaves no valid signature/disposition;
4. separate consolidated checks where needed to make the step-level result reconstructable;
5. rerun the complete frozen OQ.

### Status

`RESOLVED — PROTOCOL CONFORMANCE VERIFIED / FULL OQ PASS`

### Final conformance verification

Final run: `36813357212`  
Candidate: `37a23e1bb28c4fc96d6fcdc252d91e8a4e57ba0e`  
Frozen OQ result: **18 / 18 PASS**

A case-by-case conformance audit found:

- OQ-TC-002 through OQ-TC-018 expose the same number of explicit runner assertions as frozen numbered protocol steps;
- OQ-TC-001 expands the frozen combined post-failed-authentication check into separate invalid-password and disabled-account GxP-access assertions;
- no frozen expected result was removed or weakened.

DEV-002 is resolved. The earlier 18/18 runs produced before this apparatus correction remain useful observations but are not substituted for the final conformance-qualified execution.

## DEV-003 — Qualification evidence execution identity collision

**Training seed category:** Evidence / execution deficiency.

**Observed runs:** `36812149305` and `36812375284`

### Observation

The initial failed OQ bundle and the corrected 18/18 retest bundle were generated in separate clean GitHub Actions runs with different candidate commits, timestamps, artifact IDs, and artifact digests.

However, both bundles internally reported:

`execution_id = OQ-EXEC-001`

because the workflow used a fixed output directory and the qualification runner derived its execution ID from that directory name.

The individual evidence IDs also repeat across runs and rely on bundle context for disambiguation.

### Classification

**EVIDENCE / EXECUTION APPARATUS DEFICIENCY**

This is not a SampleTrack business-function failure and does not change the observed 18/18 behavioral result of run `36812375284`.

### Impact assessment

GitHub metadata still uniquely identifies each run through:

- workflow run ID;
- candidate commit/tree;
- execution timestamp;
- artifact ID and digest;
- source SHA-256;
- execution-file SHA-256.

Therefore the observations remain attributable.

The internal bundle identity is nevertheless insufficient for a clean standalone validation evidence package because two different executions should not claim the same execution ID.

### Root cause

The workflow hardcoded `validation/evidence/OQ-EXEC-001` as the output directory, and the runner used the output directory basename as the execution ID.

### Correction

The qualification apparatus will:

1. assign a unique execution ID from the GitHub Actions run ID;
2. use a unique evidence output directory for each run;
3. pass the execution ID explicitly to the runner;
4. include that execution ID inside every evidence JSON object;
5. preserve the frozen expected results and test logic unchanged.

### Re-test requirement

Run the complete frozen OQ once more after the evidence-identity apparatus correction.

Because the qualification runner changes, full re-execution is selected even though the change is intended to affect metadata only.

### Status

`RESOLVED — UNIQUE EXECUTION ID VERIFIED / FULL OQ PASS`

### Correction and verification receipt

The qualification apparatus now assigns the GitHub Actions run ID as a unique execution identity and includes it inside every evidence JSON object.

Verification run: `36812736825`  
Candidate: `b3ae9c728cda9d489619c6b0e72b81b43acae5ad`  
Candidate tree: `e9f322391fd785fe85d0637211a15d20e0cd53e2`  
Execution ID: `OQ-CI-36812736825`  
Development tests: **8 / 8 PASS**  
Frozen OQ case result: **18 / 18 PASS**  
Artifact: `11139832937`  
Artifact digest: `sha256:8a2b32fe35e5cd39cc7375fa21926630ae62cafa23c0096b15731807ac0cdea5`

The OQ-TC-009 evidence object was confirmed to carry `execution_id = OQ-CI-36812736825`.

## DEV-005 — Critical-data correction does not invalidate prior QA verification

**Discovered during:** public-release pressure test  
**Candidate:** `718ce8e065d78e6df7a8d837cf71c68ad3909590`  
**Candidate tree:** `f92e671a17957a262349062d137a533bb47d143c`  
**GitHub Actions run:** `36895767954`  
**Job:** `110482246469`  
**Affected requirement:** `URS-004`  
**Affected risk:** `RSK-003`

### Observation

A receiving record was successfully QA-verified for the current product, lot and storage condition. The lot was then corrected. The prior verification remained set and the system permitted release without re-verification of the corrected critical data.

The adversarial test expected release to remain blocked until the corrected critical value was independently verified.

### Classification

**SYSTEM / WORKFLOW STATE INVALIDATION FAILURE**

The application treats critical-data verification as a one-time flag rather than evidence bound to the current critical values.

### Impact

A quality release could rely on a verification performed against superseded critical data.

This invalidates final closure of URS-004 until corrected and requalified.

### Status

`RESOLVED — CORRECTED / SUCCESSOR QUALIFICATION PASS`

---

## DEV-006 — GMP status change can be recorded without required rationale

**Discovered during:** public-release pressure test  
**Candidate:** `718ce8e065d78e6df7a8d837cf71c68ad3909590`  
**GitHub Actions run:** `36895767954`  
**Affected requirement:** `URS-015`  
**Affected risks:** `RSK-005`, `RSK-015`

### Observation

A Warehouse Operator could execute a permitted `Quarantine -> On Hold` transition without supplying a reason.

The system recorded the status change with a null reason even though URS-015 requires the required reason or disposition rationale for GMP-relevant material-status changes.

### Classification

**SYSTEM / WORKFLOW DATA-INTEGRITY FAILURE**

### Impact

The resulting history can be attributable in user/time/status terms while still lacking the required reason for the change.

### Status

`RESOLVED — CORRECTED / SUCCESSOR QUALIFICATION PASS`

---

## DEV-007 — Regulated record retrieval is available without authenticated authority

**Discovered during:** public-release pressure test  
**Candidate:** `718ce8e065d78e6df7a8d837cf71c68ad3909590`  
**GitHub Actions run:** `36895767954`  
**Affected requirements:** `URS-007`, `URS-025`  
**Affected risks:** `RSK-010`, `RSK-014`

### Observation

The public application method `get_record(record_id)` returned regulated record content without receiving or validating an authenticated session.

The pressure test retrieved the SampleTrack record ID and lot without any authenticated authority.

### Classification

**SYSTEM AUTHENTICATION / AUTHORIZATION BOUNDARY FAILURE**

### Impact

The qualified surrogate's write paths had an authentication boundary, but its public read/retrieval boundary did not consistently enforce the same authority model.

Final validation consideration is blocked until regulated record retrieval paths require authenticated authority and the relevant OQ/retrieval paths are re-executed.

### Status

`RESOLVED — CORRECTED / SUCCESSOR QUALIFICATION PASS`

---

## DEV-008 — Same-status request bypasses authentication

**Discovered during:** public-release pressure test  
**Candidate:** `718ce8e065d78e6df7a8d837cf71c68ad3909590`  
**GitHub Actions run:** `36895767954`  
**Affected requirement:** `URS-025`  
**Affected risk:** `RSK-010`

### Observation

`transition_status(None, record_id, "Quarantine")` returned successfully when the record was already in Quarantine.

The function read the record and returned for the no-op case before calling its role/authentication check.

### Classification

**SYSTEM AUTHENTICATION-CHECK ORDERING FAILURE**

### Impact

The same status function that enforces authentication for state-changing paths exposes an unauthenticated execution path for a no-op request.

The observation does not itself alter material state, but it contradicts the requirement that authentication precede access to the GxP function.

### Status

`RESOLVED — CORRECTED / SUCCESSOR QUALIFICATION PASS`

---

## Public-release pressure-test execution receipt

Candidate: `718ce8e065d78e6df7a8d837cf71c68ad3909590`  
Tree: `f92e671a17957a262349062d137a533bb47d143c`  
Run: `36895767954`  
Job: `110482246469`  
Environment: Ubuntu 24.04 / x86_64 / Python 3.13.15 / SQLite 3.45.1  
Compilation: **PASS**  
Development + adversarial tests: **12 PASS / 4 FAIL / 16 total**  
Frozen OQ: **NOT ENTERED** because the adversarial gate failed.  
Artifact: `11179707347`  
Artifact ZIP SHA-256: `f8606ee2973be47b4c62e786ffc4cf25707eb44c01ed16b11fc9d313ac6d0e44`

Passing pressure controls:

- existing session invalidated after user disable;
- existing session invalidated after role change.

Failing controls are preserved above as DEV-005 through DEV-008.

Publication remains blocked until a corrected successor passes the pressure suite and the complete frozen OQ.

---

## DEV-009 — Temperature data-limit handling accepts non-finite values and leaks raw conversion errors

**Discovered during:** second public-release pressure sweep  
**Candidate:** `d1471b983d06c3564531e505dcd75f407993a52c`  
**Candidate tree:** `78b462ade0c4c3f7cd8499e7586e479638c0debf`  
**GitHub Actions run:** `36897292169`  
**Job:** `110487364234`  
**Affected requirements:** `URS-016`, `URS-017`  
**Affected risk:** `RSK-006`

### Observation

Requirement-derived data-limit/error-handling tests challenged the temperature path with:

- `NaN`;
- positive infinity;
- negative infinity;
- nonnumeric text.

Observed:

- all three non-finite numeric values were accepted rather than rejected;
- `NaN` follows comparison semantics that can appear in-range because both limit comparisons are false;
- nonnumeric text raised an uncontrolled Python `ValueError` rather than a controlled application validation error.

Pressure gate result: existing corrected controls passed, but these new data-limit cases failed before frozen OQ execution.

### Classification

**SYSTEM / INPUT-VALIDATION AND ERROR-HANDLING FAILURE**

### Impact

The excursion decision path can receive values that are not valid finite temperature measurements. In particular, a NaN value can bypass normal lower/upper comparison semantics.

This is material to the High-risk excursion-detection path and must be corrected before public release.

### Required correction

Normalize temperature input through one controlled conversion step and reject nonnumeric or non-finite values with `ValidationError` before range classification or evidence creation.

### Status

`RESOLVED — CORRECTED / SUCCESSOR QUALIFICATION PASS`

---

## DEV-010 — TC-015 QA audit-review assertion used Warehouse read authority after read-boundary hardening

**Discovered during:** public-release protocol-conformance inspection  
**Affected test:** `OQ-TC-015`  
**Affected requirement:** `URS-032`

### Observation

After the DEV-007 read-authorization correction, the automated OQ runner was updated to pass authenticated sessions to record-inspection helpers.

Inspection found that TC-015's step labelled **QA reviewability** still retrieved the audit trail using the Warehouse Operator session.

The audit content itself was exercised, but the exact frozen protocol step requiring a QA Reviewer to retrieve/review the associated audit trail was not demonstrated by that assertion.

### Classification

**QUALIFICATION APPARATUS / PROTOCOL-CONFORMANCE DISCREPANCY**

This is not evidence of a product failure. The system authorization model permits QA audit retrieval; the qualification apparatus must exercise the role specified by the frozen protocol.

### Required correction

Retrieve the audit trail with `QA_REVIEW_01` for the frozen QA-reviewability step and preserve the complete successor run.

### Status

`RESOLVED — CORRECTED / SUCCESSOR QUALIFICATION PASS`

---

## Second public-release pressure-sweep receipt

Candidate: `d1471b983d06c3564531e505dcd75f407993a52c`  
Tree: `78b462ade0c4c3f7cd8499e7586e479638c0debf`  
Run: `36897292169`  
Job: `110487364234`  
Environment: Ubuntu 24.04 / x86_64 / Python 3.13.15 / SQLite 3.45.1  
Compilation: **PASS**  
Development/adversarial suite: original and first-wave pressure controls passed; non-finite/malformed temperature tests failed.  
Frozen OQ: **NOT ENTERED** because the pressure gate failed.  
Artifact: `11179849851`  
Artifact ZIP SHA-256: `c137814080ba4cfa35169471d4ef19e8ab3cad722d495acfeaf091a52a9e8f9f`

---

## Final deviation closure summary

Successor qualification: `OQ-CI-36897449285` on exact application/runner candidate `b528234a0a14db68200c9213516d0ed6a76ca56b`.

- compilation: **PASS**
- expanded development/adversarial suite: **18 / 18 PASS**
- unchanged frozen OQ: **18 / 18 PASS**
- open validation deviations: **0**
- no frozen expected result was changed to obtain the pass

DEV-005 through DEV-010 are resolved for the successor candidate. Earlier failed runs remain preserved in this log.

## DEV-011 — Receiving record can complete without required receipt date

**Discovered during:** final source-to-URS public-release pressure test  
**Candidate:** `915e3f7215c33fdc2646c74ae168c94080fdf306`  
**Candidate tree:** `22baa35067b994399744875fd4889f5eeb037851`  
**GitHub Actions run:** `36946957100`  
**Job:** `110651165310`  
**Affected requirement:** `URS-002`  
**Affected risk:** `RSK-002`

### Observation

URS-002 requires a receiving record to contain a distinct **receipt date** before completion.

The demonstration surrogate accepted and completed a receiving record through:

`create_inventory(session, product_id, lot, quantity, storage_condition)`

without any receipt-date field or receipt-date completion gate.

The pressure-test challenge expected the missing receipt date to raise `ValidationError`; no exception was raised.

Run result:

- frozen-authority guard: **PASS**
- compilation: **PASS**
- development/adversarial tests: **18 PASS / 1 FAIL**
- frozen OQ: **NOT ENTERED**

### Classification

**SYSTEM / REQUIRED-DATA COMPLETENESS FAILURE**

There is also a **qualification-coverage gap**: the frozen OQ and test fixture did not separately exercise the receipt-date element of URS-002.

The frozen URS remains authoritative and is not weakened or reinterpreted to make the implementation pass.

### Impact assessment

A receiving record could be considered complete while omitting one of the explicitly required receiving fields.

This prevents continued final closure of URS-002 and RSK-002 for the current candidate.

The system-generated creation timestamp is not silently substituted for the separately specified receipt date.

### Required correction

- add a distinct required receipt-date field to the receiving record;
- validate receipt date as a controlled ISO calendar date;
- retain it in the authoritative record and human-readable/electronic outputs;
- update valid demonstration callers to provide the frozen-scenario receipt date;
- add supplemental adversarial verification for missing, malformed, and retained receipt date;
- rerun the complete expanded pressure suite and unchanged frozen OQ.

### Status

`RESOLVED — REQUIRED RECEIPT DATE ADDED / SUCCESSOR QUALIFICATION PASS`

### Correction and successor qualification

The surrogate now:

- requires a distinct receipt date before receiving completion;
- validates the supplied value as an ISO calendar date;
- retains the normalized receipt date in the authoritative receiving record;
- includes it in electronic and human-readable record output;
- preserves system creation time separately from the business receipt date.

Supplemental pressure verification challenges:

- missing receipt date;
- malformed receipt date;
- valid receipt-date retention;
- electronic-copy retention;
- human-readable output.

Successor candidate: `df40d5b71517e30af425d3b0f02e4e05c920cca6`  
Candidate tree: `14431f747e3072435f7664263724cd10c3365da1`  
GitHub Actions run: `36947244505`  
Job: `110652043880`  
Development/adversarial suite: **19 / 19 PASS**  
Unchanged frozen OQ: **18 / 18 PASS**  
`sampletrack.py` SHA-256: `f61136b70b020d1516470c263308750427ac65fff621be73dacf824ef70a35d0`  
`test_sampletrack.py` SHA-256: `36b0f41d79476d9f42f412e33a20f71de2840ea5c3eee4c2adb1895589d1928a`  
`test_pressure.py` SHA-256: `dc35140bde0618f769f3897d31debad643c2e7c581b1d63f03bfe802f636df94`  
`oq_runner.py` SHA-256: `982a635c3fff19e942401e272cba5f2c061572c614d192951b4f44632c7bbf37`  
Artifact ID: `11203030254`  
Artifact ZIP SHA-256: `45c51df8787a32a5851ee6895d89a4c7bfc3e424364b49019f08ebe232b28845`

DEV-011 is resolved for this exact successor candidate. The failed 18/1 run remains preserved.

### Preserved failure receipt

Artifact ID: `11202038732`  
Artifact ZIP SHA-256: `1b8bde6ab6122ba979c8a73e04db0e2b2b1efde10fcdc83c2249d7cf344b0adb`

Publication remains blocked until DEV-011 is resolved by an exact successor candidate.

---

## Pre-execution apparatus incident — workflow checkout

Before OQ-EXEC-001, GitHub Actions run `36811955161` failed at candidate checkout because the workflow supplied an escaped SHA ref.

No system-under-test code executed. No OQ evidence was produced.

Classification: **APPARATUS FAILURE — PRE-EXECUTION**.

The workflow-only correction did not change the frozen validation artifacts or the system-under-test source blobs, so this incident does not invalidate OQ-EXEC-001.

## Revision history

| Revision | Status | Description |
|---|---|---|
| 0.1 | Active | DEV-001 opened from preserved first OQ execution; pre-execution workflow incident recorded separately. |
| 0.2 | Active | DEV-001 corrected and full retest passed; DEV-003 opened for duplicate internal execution identity across evidence bundles. |
| 0.3 | Active | DEV-003 resolved with unique execution identity; DEV-002 opened after frozen-protocol-to-runner step-coverage audit. |
| 0.4 | Active | DEV-004 opened after corrected harness exposed uncontrolled unauthenticated-access behavior; adversarial pre-correction tests added. |
| 0.5 | Active | DEV-004 adversarial test confirmed forged-session authorization bypass; session authority correction applied pending full qualification. |
| 0.6 | Closed for qualified candidate | DEV-002 and DEV-004 closed by exact-candidate run 36813357212; all four recorded validation deviations resolved with failed evidence preserved. |
| 0.7 | Closed / supplemented | Added local preservation receipt for original fed1f956 candidate; corroborates DEV-001 defect while preserving unknown historical environment/invocation limits. |
| 0.8 | Reopened | Public-release pressure test run 36895767954 found four requirement-level gaps; DEV-005 through DEV-008 opened and publication blocked pending successor qualification. |
| 0.9 | Reopened | Second pressure sweep found temperature data-limit failure (DEV-009) and QA-review apparatus discrepancy (DEV-010); full successor qualification required. |
| 1.0 | Closed for successor candidate | DEV-005 through DEV-010 resolved; expanded pressure suite 18/18 PASS and unchanged frozen OQ 18/18 PASS. |
| 1.1 | Reopened | Final source-to-URS pressure test exposed missing required receipt-date control as DEV-011; OQ not entered and publication blocked. |
| 1.2 | Closed for successor candidate | DEV-011 resolved; expanded suite 19/19 PASS and unchanged frozen OQ 18/18 PASS on exact candidate df40d5b. |
