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

`OPEN — APPARATUS CORRECTION APPLIED / FULL RETEST REQUIRED`

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
