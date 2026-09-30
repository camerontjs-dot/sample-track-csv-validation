# SampleTrack Lite Mock CSV Package Plan

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

## 1. Objective

Build a compact, risk-based computerized system validation package for **SampleTrack Lite**, a fictional configured product used in a GMP pharmaceutical warehouse/distribution scenario.

The package is intended to demonstrate how intended use, regulatory applicability, requirements, risk, verification evidence, deviations, traceability, and a final validation decision fit together.

It is not evidence that SampleTrack Lite is suitable for real GxP use, and it does not represent prior ownership of a production CSV program.

## 2. Validation scenario

SampleTrack Lite is treated as a **configured commercial product** for purposes of the exercise. The scenario assumes that:

- the supplier owns and maintains the base product;
- the regulated company configures roles, workflow states, storage locations, excursion thresholds, and approval behavior;
- supplier source code is not modified by the regulated company;
- the intended validation approach is therefore consistent with a GAMP 5 Category 4 configured-product scenario.

This categorization is a scenario design assumption. It is not a regulatory designation and does not establish anything about a real supplier product.

## 3. Package deliverables

| ID | Deliverable | Intended role |
|---|---|---|
| STL-SD-001 | System Description and Intended Use | Establish the system, boundary, GxP use, records, users, and important assumptions. |
| STL-RA-001 | Regulatory Applicability Statement | Establish which regulations/guidance govern the mock scenario and which are conditional references. |
| STL-VP-001 | Validation Plan | Define lifecycle scope, roles, deliverables, risk/test strategy, acceptance, and deviation handling. |
| STL-RAK-001 | Risk Assessment | Identify failure modes and use risk to determine verification depth. |
| STL-URS-001 | User Requirements Specification | Define approximately 30-35 testable regulated-user requirements. |
| STL-RTM-001 | Requirements Traceability Matrix | Trace requirements to risk, tests, evidence, deviations, and final status. |
| STL-OQ-001 | Operational Qualification | Predefine and execute approximately 18 risk-based test cases. |
| STL-DEV-001 | Validation Deviation Log | Preserve three seeded training deviations with impact assessment, correction, and disposition. |
| STL-VSR-001 | Validation Summary Report | Summarize execution and make a bounded mock release decision. |

Current work status belongs in GitHub Issue #1 and pull requests rather than this plan.

## 4. Build sequence

1. System Description and Intended Use.
2. Regulatory Applicability Statement.
3. Draft Validation Plan.
4. User Requirements Specification.
5. Risk Assessment, with URS/risk iteration where justified.
6. Finalize Validation Plan and acceptance criteria.
7. Create the initial traceability matrix.
8. Design OQ tests from requirements and risk.
9. Freeze the decisive OQ expectations, inputs, and acceptance criteria.
10. Execute OQ and preserve first-run evidence.
11. Record and disposition seeded training deviations without erasing failed evidence.
12. Re-execute affected tests where justified.
13. Close traceability.
14. Write the Validation Summary Report.
15. Perform package-level consistency and mock-watermark review.

## 5. Evidence model

The package should maintain a reconstructable chain:

```text
intended use
  -> regulatory / GxP impact
  -> user requirement
  -> failure mode / risk
  -> verification depth
  -> test case
  -> observed evidence
  -> deviation / correction / retest where applicable
  -> traceability closure
  -> bounded validation decision
```

A passing test is evidence only for the behavior it actually exercises. Material failed executions remain part of the package after repair.

## 6. Risk-based verification posture

The risk assessment will use Severity, Probability, and Detectability ratings as a structured prioritization tool. Numerical scoring will not replace judgment.

High-consequence failure modes may receive a severity override or enhanced test depth even when a simple RPN would otherwise reduce their rank.

Expected high-risk areas include:

- incorrect material status or disposition;
- failure to detect or flag a temperature excursion;
- unauthorized record or status change;
- loss or corruption of chain-of-custody history;
- audit-trail failure;
- broken electronic-signature linkage;
- failure to retrieve required regulated records.

Lower-risk presentation or convenience functions should receive proportionally lighter verification.

## 7. OQ execution rule

Before decisive OQ execution, the relevant URS, risk decisions, test steps, expected results, and acceptance criteria should be stable enough that a failing result cannot simply be rewritten into a pass.

If a test reveals:

- a system/configuration defect,
- a protocol discrepancy,
- an evidence deficiency, or
- an invalid test apparatus,

the first result should be preserved and the deviation classified. Corrections and retesting should be traceable to the affected requirement and risk.

## 8. Planned seeded training deviations

The package is expected to include three transparently seeded deviations:

1. **System/configuration defect:** a temperature-excursion threshold or status-control configuration behaves incorrectly.
2. **Protocol/document discrepancy:** the test script contains an incorrect role or configured-label reference while the system requirement remains correct.
3. **Evidence/execution deficiency:** initial evidence does not adequately establish a required test condition or result and the affected step must be re-executed.

They must be labelled as training seeds. They must not be presented as accidental production events.

## 9. Document and evidence identifiers

Use stable IDs rather than filenames alone.

Examples:

- `STL-URS-012`
- `STL-RISK-007`
- `STL-OQ-TC-014`
- `STL-DEV-002`
- `STL-EV-OQ-014-01`

Evidence filenames may include the stable ID, execution date, and a short description.

## 10. Mock-document controls

Every controlled validation deliverable and execution artifact should include:

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

Do not create fictional QA approvers, company authorization, or handwritten/electronic signatures.

Where a real validation package would require approval, use a clear non-executed field such as:

`Mock approval: Not executed`

A real tester name and real execution date may be used only for work actually executed by the repository owner against the demonstration environment.

## 11. Twenty-hour core target

The core package should optimize for evidence density rather than document volume.

Approximate planning budget:

| Activity | Target |
|---|---:|
| System description + applicability | 2.0-2.5 h |
| Validation Plan | 1.5-2.0 h |
| URS | 2.5-3.0 h |
| Risk Assessment | 2.0-2.5 h |
| RTM | 1.0 h |
| OQ design, execution, evidence | 5.0-6.0 h |
| Deviation handling | 1.0 h |
| VSR | 1.5 h |
| Package QC / interview path | 1.0 h |

If time is constrained, reduce low-risk test count and cosmetic formatting before removing traceability, deviation handling, risk rationale, or the final decision record.

## 12. Optional add-ons

### Demonstration surrogate

A small runnable Python application may later be built to provide genuine execution behavior.

If implemented, it must be described as a **custom demonstration surrogate** used to exercise the validation artifacts. It must not be used as evidence that the fictional SampleTrack Lite supplier product is GAMP Category 4.

### Evidence checksum manifest

A small script may generate SHA-256 digests for screenshots, exports, and other execution evidence.

Checksums establish evidence-object identity/integrity. They do not establish that the underlying test result is correct.

## 13. Public-facing boundary

If this repository is later made public, technical artifacts should describe what was exercised, what failed, what evidence exists, and what is not established.

Do not add evaluator-facing sections such as "skills demonstrated" or imply that the mock package is equivalent to regulated on-the-job CSV experience.
