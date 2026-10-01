# STL-VSR-001 — SampleTrack Lite Validation Summary Report

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Document ID | STL-VSR-001 |
| Title | SampleTrack Lite Validation Summary Report |
| System | SampleTrack Lite demonstration surrogate |
| Document status | Final mock validation summary |
| Final disposition | ACCEPTED FOR BOUNDED MOCK DEMONSTRATION USE |
| Production disposition | NOT APPROVED FOR GxP PRODUCTION USE |
| Approval status | Mock approval: Not executed |

## 1. Purpose

This Validation Summary Report summarizes the evidence generated for the SampleTrack Lite mock computerized-system validation exercise and records the final bounded validation decision.

The report evaluates whether the exact custom demonstration surrogate satisfied the frozen functional validation scope defined by the mock package.

It does not establish that a real supplier product has been validated, that a production environment has been qualified, or that any real pharmaceutical operation may rely on this surrogate for GxP use.

## 2. System and candidate identity

Validation scenario:

- fictional SampleTrack Lite configured-product scenario;
- custom Python/SQLite demonstration surrogate used only to generate genuine execution evidence.

Exact qualified system-under-test candidate:

- commit: `37a23e1bb28c4fc96d6fcdc252d91e8a4e57ba0e`
- tree: `0fd797f7a4532ef18284aa8484c2db7036532c02`
- `demo/sampletrack.py` SHA-256: `c0bcf3919279d41aabe90f63056f8b63b57e38f3ca8a3d146ab5a128ea28afe4`
- `demo/test_sampletrack.py` SHA-256: `a3318e9522b01e1e77d4db9247af2085cf89836121737301378350de6e6735e1`
- `demo/oq_runner.py` SHA-256: `0789c67da040a73904602b3ef0638e3ed27adca72268c180b92ffdf207ce68af`

The repository branch later advanced through documentation-only reconciliation commits.

A direct Git blob comparison confirmed that the current branch copies of the application, development tests, and OQ runner remain byte-identical to the exact tested candidate.

## 3. Governing validation package

The final decision is based on:

- STL-SD-001 — System Description and Intended Use
- STL-RA-001 — Regulatory Applicability Statement
- STL-VP-001 — Validation Plan
- STL-URS-001 — User Requirements Specification
- STL-RSK-001 — Functional Risk Assessment
- STL-RTM-001 — Requirements Traceability Matrix
- STL-OQ-001 — Operational Qualification Protocol
- STL-OQ-001 — Test Configuration and Data Set
- STL-OQ-001 — Protocol Freeze Record
- STL-OQ-001 — Execution Readiness Record
- STL-DL-001 — Validation Deviation Log
- STL-OQ-001 — Final Qualification Receipt
- preserved GitHub Actions execution evidence

The OQ protocol and test oracle were frozen before implementation qualification.

## 4. Regulatory and guidance basis

The package was designed primarily against the Canadian GMP scenario defined in STL-RA-001.

Primary sources included:

- Health Canada GUI-0001;
- Health Canada GUI-0050, Annex 11 to the GMP Guide: Computerized Systems;
- Health Canada GUI-0069 for environmental control during storage and transportation.

GAMP 5 Second Edition was used as industry lifecycle/risk guidance.

Selected 21 CFR Part 11 controls were included as a conditional electronic-record/electronic-signature exercise overlay. U.S. legal applicability was not asserted.

A pre-OQ source review identified and corrected a requirement gap before execution: URS-007 was expanded to require accurate and complete record copies in both human-readable and electronic form because the package explicitly mapped that requirement to Part 11 §11.10(b).

No frozen expected result was changed after observing OQ behavior in order to obtain the final passing disposition.

## 5. Validation scope executed

The mock qualification exercised:

- authentication and disabled-account behavior;
- unique user identity and role-based authority;
- receiving and inventory record creation;
- critical manually entered data verification;
- storage-condition and location compatibility;
- controlled material statuses and permitted transitions;
- temperature-excursion boundary detection;
- excursion hold and QA disposition;
- chain-of-custody history;
- GMP-relevant audit-trail behavior;
- electronic-signature manifestation, authentication, attribution, and record linkage;
- regulated-record retrieval;
- human-readable and electronic record copies;
- end-to-end receipt through excursion and disposition.

Formal production IQ and PQ were not executed.

## 6. Execution environment

Final full OQ:

- GitHub Actions run: `36813357212`
- job: `110213023142`
- execution ID: `OQ-CI-36813357212`
- executed: 2026-10-01T04:03:52+00:00
- GitHub-hosted Ubuntu 24.04 runner
- architecture: x86_64
- Python: 3.13.15
- SQLite: 3.45.1

The workflow checked out the exact candidate in detached-HEAD state.

## 7. Execution ownership and independence

The final OQ was executed automatically by GitHub Actions against the exact pinned repository candidate.

The `Tester: Cameron` field in the generated execution record identifies the exercise owner/protocol operator. It does **not** mean Cameron manually performed each automated test step.

Independence is limited:

- the OQ requirements and expected results were frozen before the demonstration surrogate was qualified;
- GitHub Actions provided a clean hosted execution environment against exact committed code;
- however, the surrogate implementation, automated qualification runner, and validation package were developed within the same overall project;
- the final OQ is therefore reproducible behavioral evidence, but not an organizationally independent validation or independent second implementation.

This limitation is retained in the final claim rather than describing CI execution as independent QA approval.

## 8. Development verification

Before final OQ execution:

- Python compilation: **PASS**
- development tests: **10 / 10 PASS**

The development suite included targeted regression/adversarial checks for:

- inclusive 8.0 °C upper boundary behavior;
- controlled denial of unauthenticated GxP writes;
- rejection of a caller-constructed forged session;
- authentication and disabled-account behavior;
- storage compatibility;
- QA authority;
- audit-trail protection;
- electronic-signature credential enforcement.

These tests supplement but do not replace OQ.

## 9. Operational Qualification result

Final frozen OQ result:

| Measure | Result |
|---|---:|
| Planned OQ cases | 18 |
| Executed OQ cases | 18 |
| PASS | 18 |
| FAIL | 0 |
| Open OQ deviations | 0 |

The final execution includes the complete frozen behavior set.

OQ-TC-001 expands one combined frozen step into separate invalid-password and disabled-account post-failure GxP-access checks. This increases inspectability without changing the expected behavior.

### Evidence identity

GitHub Actions artifact:

- artifact ID: `11140757299`
- artifact: `sampletrack-oq-36813357212`
- artifact ZIP SHA-256: `94f82fb01bdd9999c4d71ccbd2587702181ab45bf7833dc39cb987b16051a490`

Core execution hashes:

- `execution.json`: `33fa401498126a58369b57226d1856bb97ae92548a0c15d2d081e6eec04186cd`
- `execution.md`: `65956cd5541b3efc6a24e7a81cc7945c685e34a5d4ae20fc900bdca2f1d833c3`
- `manifest.json`: `0318f5f73106054e3a1f95d83a08c258af10e75d625454eca7a69ce42f01204a`

Individual evidence IDs and hashes are preserved in the execution manifest and final qualification receipt.

## 10. Validation deviations

Four validation deviations were preserved during qualification.

### DEV-001 — Upper temperature boundary defect

Initial OQ observed:

- expected 8.0 °C: Within range;
- actual: Excursion.

Classification: system/configuration failure.

The defect was corrected without modifying the frozen expected result, and the complete OQ was rerun.

Final status: **RESOLVED**.

### DEV-002 — Qualification harness protocol coverage

The first automated OQ harness did not expose every frozen protocol step with sufficient step-level clarity.

Classification: protocol/execution-apparatus discrepancy.

The runner was reconciled to the frozen protocol and the complete OQ was rerun.

Final status: **RESOLVED**.

### DEV-003 — Duplicate execution identity

Separate qualification bundles initially reused the same internal execution ID.

Classification: evidence/execution-apparatus deficiency.

Unique GitHub-run-derived execution IDs were added and the complete OQ was rerun.

Final status: **RESOLVED**.

### DEV-004 — Authentication authority boundary

Corrected harness coverage exposed an uncontrolled unauthenticated access failure. Requirement-derived adversarial tests then confirmed a forged-session authorization path.

Classification: system authentication/authorization boundary failure.

The surrogate was corrected to use application-issued opaque session authority, validate session state, reject absent/forged/stale sessions, and invalidate session authority when access changes.

Final candidate passed the adversarial development tests and full OQ.

Final status: **RESOLVED**.

### Pre-execution apparatus incident

GitHub Actions run `36811955161` failed during checkout because of an escaped SHA ref.

No system-under-test code or OQ step executed.

Classification: **pre-execution apparatus failure**.

This incident is preserved separately and is not treated as a SampleTrack functional result.

## 11. Requirements traceability

Final RTM status:

- URS requirements: **35 / 35 represented**
- requirements with risk linkage: **35 / 35**
- requirements with final OQ evidence: **35 / 35**
- final requirement status: **35 / 35 VERIFIED — PASS**
- open validation deviations: **0**

Requirement-specific deviation history remains visible for the affected temperature and authentication controls.

The RTM references exact final evidence IDs rather than using the aggregate green OQ result as a substitute for traceability.

## 12. Functional risk disposition

Design-time risk assessment:

- High: 9
- Medium: 4
- Low: 2

The original Severity, Probability, Detectability, RPN, and class values remain unchanged after testing.

Following final OQ:

- all 15 functional risks have at least one executed verification path;
- the associated application controls are marked **SUPPORTED WITH BOUNDS — OQ-CI-36813357212 PASS**.

A successful OQ does not mean the risks cease to exist or that real production probability has been measured.

## 13. Validation Plan acceptance criteria

| Acceptance criterion | Final status | Evidence basis |
|---|---|---|
| Final in-scope URS uniquely identified | PASS | STL-URS-001, 35 requirements |
| Every in-scope URS traced or explicitly dispositioned | PASS | STL-RTM-001, 35/35 |
| All planned OQ tests executed or formally dispositioned | PASS | OQ-CI-36813357212, 18/18 executed |
| High-risk functions receive risk-proportionate verification | PASS | STL-RSK-001 V3 paths; final OQ |
| No unresolved deviation invalidates a high-risk requirement or conclusion | PASS | STL-DL-001, 0 open deviations |
| Failed tests corrected through impact assessment and justified retest | PASS | DEV-001 through DEV-004 lineage |
| Access, status, excursion, audit, e-signature, and record-retrieval controls meet applicable criteria | PASS | Final 18/18 OQ evidence |
| Tested system/configuration identity known | PASS | exact commit/tree/source SHA-256 |
| RTM reflects final executed evidence | PASS | STL-RTM-001 executed/reconciled revision |
| Residual risks and untested production dependencies explicit | PASS | STL-RSK-001 and this VSR |

Formal organizational QA approval is intentionally not fabricated.

## 14. Residual limitations

The following were not established by this mock package:

- supplier quality-system qualification;
- validation of a real commercial configured product;
- production server/cloud/network/database qualification;
- formal installation qualification of real infrastructure;
- formal PQ under actual warehouse operating conditions;
- backup/restore qualification;
- long-term archive accessibility and retention;
- production business-continuity/disaster-recovery performance;
- real SOP and training effectiveness;
- cybersecurity assessment or penetration testing;
- production workload/performance;
- real sensor/logger qualification;
- warehouse temperature mapping;
- pharmaceutical stability or scientific acceptability of a real temperature excursion;
- actual Canadian, U.S., or EU regulatory compliance;
- FDA Part 11 jurisdiction;
- production deployment.

These are boundaries, not hidden assumptions that are being treated as passed.

## 15. Final validation decision

### Disposition

**ACCEPTED FOR BOUNDED MOCK DEMONSTRATION USE**

Within the defined fictional scenario, the exact custom demonstration surrogate candidate `37a23e1bb28c4fc96d6fcdc252d91e8a4e57ba0e` satisfied the frozen functional URS/OQ acceptance criteria after documented correction and requalification of the observed validation deviations.

### Production decision

**NOT APPROVED FOR GxP PRODUCTION USE**

This package does not qualify SampleTrack Lite, the demonstration surrogate, or any real computerized system for regulated production use.

The final claim is limited to the tested mock functional boundary.

## 16. Revalidation / reconsideration triggers

The bounded disposition should be reconsidered if any of the following materially change:

- application source or validated behavior;
- authentication/session authority;
- roles or permissions;
- material-status workflow;
- storage conditions or location rules;
- excursion thresholds or comparison logic;
- audit-trail behavior;
- electronic-signature behavior;
- persistence/data representation;
- external interfaces;
- qualification runner or evidence semantics;
- frozen URS/risk/OQ authority;
- regulatory requirements applicable to the intended use.

A documentation-only change does not automatically require requalification, but its impact should be assessed if it changes interpretation of the validation claim.

## 17. Conclusion

The mock package achieved its intended demonstration objective:

```text
intended use
  → regulatory applicability
  → user requirements
  → functional risk
  → frozen OQ
  → preserved failure
  → deviation / correction / retest
  → final evidence
  → traceability closure
  → bounded validation decision
```

The evidence supports the bounded mock disposition above and no broader claim.

## 18. References

- STL-RA-001 — Regulatory Applicability Statement
- STL-VP-001 — Validation Plan
- STL-RSK-001 — Functional Risk Assessment
- STL-RTM-001 — Requirements Traceability Matrix
- STL-DL-001 — Validation Deviation Log
- STL-OQ-001 — Final Qualification Receipt
- GitHub Actions run `36813357212`

## 19. Revision history

| Revision | Status | Description |
|---|---|---|
| 1.0 | Final mock summary | Final bounded validation decision for exact qualified candidate after complete deviation reconciliation. |
| 1.1 | Final mock summary | Clarified automated execution ownership, limited independence, and non-executed mock approval boundary. |
