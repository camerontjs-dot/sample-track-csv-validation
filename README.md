# CSV-demo

Mock computerized system validation (CSV) package for **SampleTrack Lite**, a fictional configured sample/inventory tracking system used in a GMP pharmaceutical warehouse/distribution scenario.

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

This repository contains a bounded validation exercise built from intended use through final traceability and validation summary. It does **not** represent production validation work, a validated commercial system, or prior ownership of a formal CSV program.

## Current bounded result

Exact qualified custom demonstration surrogate:

`37a23e1bb28c4fc96d6fcdc252d91e8a4e57ba0e`

Observed for the final qualification run:

- development tests: **10 / 10 PASS**;
- frozen OQ: **18 / 18 PASS**;
- URS traceability: **35 / 35 VERIFIED — PASS**;
- recorded validation deviations: **4 / 4 resolved**;
- final mock disposition: **ACCEPTED FOR BOUNDED MOCK DEMONSTRATION USE**;
- production disposition: **NOT APPROVED FOR GxP PRODUCTION USE**.

The successful final run does not erase the preserved failed executions that preceded it.

## Start here

- [Validation package index](validation/README.md)
- [System Description and Intended Use](validation/STL-SD-001-system-description-intended-use.md)
- [Regulatory Applicability Statement](validation/STL-RA-001-regulatory-applicability.md)
- [Validation Plan](validation/STL-VP-001-validation-plan.md)
- [User Requirements Specification](validation/STL-URS-001-user-requirements.md)
- [Functional Risk Assessment](validation/STL-RSK-001-functional-risk-assessment.md)
- [Executed Requirements Traceability Matrix](validation/STL-RTM-001-requirements-traceability-matrix.md)
- [Operational Qualification Protocol](validation/STL-OQ-001-operational-qualification.md)
- [Validation Deviation Log](validation/STL-DL-001-validation-deviation-log.md)
- [Final Qualification Receipt](validation/STL-OQ-001-final-qualification-receipt.md)
- [Validation Summary Report](validation/STL-VSR-001-validation-summary-report.md)
- [Final step-level OQ execution record](validation/evidence/OQ-CI-36813357212/execution.md)
- [Package plan](docs/VALIDATION-PACKAGE-PLAN.md)

## Scenario boundary

SampleTrack Lite is treated as a fictional **configured commercial product** for the validation scenario. That Category 4 assumption is part of the exercise and is not a claim about a real supplier product.

Canadian GMP and Health Canada computerized-system/storage guidance are the primary regulatory basis. Selected 21 CFR Part 11 controls are included as a conditional electronic-record/e-signature exercise overlay; U.S. legal applicability is not asserted.

The runnable Python/SQLite implementation in `demo/` is a **custom demonstration surrogate** used to produce real test evidence against the frozen protocol. It is not the fictional Category 4 supplier product.

## Evidence chain

The repository maintains a reconstructable path:

```text
intended use
  -> regulatory / GxP impact
  -> user requirement
  -> risk
  -> verification depth
  -> frozen OQ
  -> observed failure
  -> deviation / correction / retest
  -> final execution evidence
  -> traceability closure
  -> bounded validation decision
```

Material failures remain visible after correction.

The final GitHub Actions execution is identified by:

- run: `36813357212`;
- execution ID: `OQ-CI-36813357212`;
- evidence artifact SHA-256: `94f82fb01bdd9999c4d71ccbd2587702181ab45bf7833dc39cb987b16051a490`.

See the Validation Summary Report for scope, residual limitations, and the final bounded decision.
