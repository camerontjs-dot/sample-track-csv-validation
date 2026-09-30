# CSV-demo

Mock computerized system validation (CSV) package for **SampleTrack Lite**, a fictional configured sample/inventory tracking system used in a GMP pharmaceutical warehouse/distribution scenario.

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

This repository is intentionally being built as an inspectable validation exercise. It does not represent production validation work, a validated system, or prior ownership of a formal CSV program.

## Start here

- [Validation package plan](docs/VALIDATION-PACKAGE-PLAN.md)
- [Validation package index](validation/README.md)
- [STL-SD-001 — System Description and Intended Use](validation/STL-SD-001-system-description-intended-use.md)
- [STL-RA-001 — Regulatory Applicability Statement](validation/STL-RA-001-regulatory-applicability.md)
- [Issue #1 — package workstream](https://github.com/camerontjs-dot/CSV-demo/issues/1)

## Scenario boundary

SampleTrack Lite is treated as a fictional **configured commercial product** for the validation scenario. That Category 4 assumption is part of the exercise and is not a claim about a real supplier product.

Canadian GMP and Health Canada computerized-system/storage guidance are the primary basis. Selected 21 CFR Part 11 controls are included as a conditional electronic-record/e-signature exercise overlay; U.S. legal applicability is not asserted.

If a runnable Python application is added later, it will be identified as a **custom demonstration surrogate**, not as the Category 4 product described by the validation package.

## Evidence posture

The package will be developed through controlled pull requests so requirements, risk decisions, test evidence, deviations, and final conclusions remain reconstructable.

The target evidence chain is:

```text
intended use
  -> regulatory / GxP impact
  -> user requirement
  -> risk
  -> verification depth
  -> executed test evidence
  -> deviation / correction / retest
  -> traceability closure
  -> bounded validation decision
```

Failed or inconvenient execution evidence will not be rewritten out of the record after correction.
