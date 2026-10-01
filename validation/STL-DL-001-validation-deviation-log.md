# STL-DL-001 — SampleTrack Lite Validation Deviation Log

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Document ID | STL-DL-001 |
| System | SampleTrack Lite demonstration surrogate |
| Status | Active |
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

`OPEN — FORGED-SESSION BYPASS CONFIRMED / CORRECTION APPLIED / FULL RETEST REQUIRED`

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

`OPEN — HARNESS CORRECTION APPLIED / FULL OQ RETEST REQUIRED`

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
