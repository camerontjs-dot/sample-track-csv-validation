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

`OPEN — CORRECTION AUTHORIZED / RETEST REQUIRED`

The original run and evidence must remain preserved after correction.

## Pre-execution apparatus incident — workflow checkout

Before OQ-EXEC-001, GitHub Actions run `36811955161` failed at candidate checkout because the workflow supplied an escaped SHA ref.

No system-under-test code executed. No OQ evidence was produced.

Classification: **APPARATUS FAILURE — PRE-EXECUTION**.

The workflow-only correction did not change the frozen validation artifacts or the system-under-test source blobs, so this incident does not invalidate OQ-EXEC-001.

## Revision history

| Revision | Status | Description |
|---|---|---|
| 0.1 | Active | DEV-001 opened from preserved first OQ execution; pre-execution workflow incident recorded separately. |
