# Sample Track CSV Validation

> **MOCK / FICTIONAL - DEMONSTRATION ONLY - NOT FOR GxP USE**

This repository is a bounded computerized system validation (CSV) exercise for **SampleTrack Lite**, a fictional sample and inventory tracking system in a pharmaceutical warehouse/distribution scenario.

It follows one validation thread from intended use through requirements, risk, frozen qualification, observed failures, controlled correction, traceability closure, and a final bounded decision.

It does **not** establish production validation, regulatory compliance, supplier qualification, or suitability for real GxP use.

## Current bounded result

Exact qualified custom demonstration surrogate:

`df40d5b71517e30af425d3b0f02e4e05c920cca6`

Final qualification evidence:

- development and adversarial pressure tests: **19 / 19 PASS**;
- frozen OQ: **18 / 18 PASS**;
- URS traceability: **35 / 35 VERIFIED - PASS**;
- recorded validation deviations: **11 / 11 resolved**;
- final mock disposition: **ACCEPTED FOR BOUNDED MOCK DEMONSTRATION USE**;
- production disposition: **NOT APPROVED FOR GxP PRODUCTION USE**.

The passing final run does not replace the failed executions that preceded it. The failure and correction lineage remains part of the validation record.

## What the pressure test added

A separate pre-publication adversarial pass challenged behaviors beyond the original OQ examples. It found additional defects in stale verification state, status-change rationale, regulated read authorization, authentication ordering, malformed temperature handling, and one qualification-role mismatch.

Those findings were preserved as DEV-005 through DEV-010. A final source-to-URS pass then found DEV-011: receiving could complete without the distinct receipt date required by URS-002. Publication remained blocked until the corrected successor passed the expanded 19-test pressure suite and the unchanged 18-case frozen OQ.

## Reproduce the demonstration

The surrogate uses Python's standard library and SQLite. No third-party Python package is required.

Development tests:

```bash
cd demo
python3 -m unittest discover -v
```

Run the automated OQ harness locally:

```bash
cd demo
python3 oq_runner.py \
  --output ../local-oq-output \
  --tester "local-reproduction" \
  --system-identity "local-working-copy" \
  --execution-id "LOCAL-OQ-001"
```

A local reproduction is useful behavioral evidence, but it is not the authoritative final qualification run. The final qualified candidate and evidence identities are recorded below and in the validation package.

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
- [Current Public-Release Pressure Qualification Receipt](validation/STL-OQ-001-public-release-pressure-qualification.md)
- [Historical pre-pressure qualification receipt](validation/STL-OQ-001-final-qualification-receipt.md)
- [Validation Summary Report](validation/STL-VSR-001-validation-summary-report.md)
- [Current step-level OQ execution record](validation/evidence/OQ-CI-36947244505/execution.md)
- [Original package plan](docs/VALIDATION-PACKAGE-PLAN.md)

## Scenario boundary

SampleTrack Lite is treated as a fictional **configured commercial product** for the validation scenario. That Category 4 assumption belongs to the scenario and is not a claim about a real supplier product.

Canadian GMP and Health Canada computerized-system/storage guidance are the primary regulatory basis. Selected 21 CFR Part 11 controls are included as a conditional electronic-record/e-signature exercise overlay; U.S. legal applicability is not asserted.

The runnable Python/SQLite implementation in `demo/` is a **custom demonstration surrogate** used to produce real execution evidence against the frozen protocol. It is not the fictional Category 4 supplier product.

## Evidence chain

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

Final GitHub Actions execution:

- run: `36947244505`;
- execution ID: `OQ-CI-36947244505`;
- exact qualified commit: `df40d5b71517e30af425d3b0f02e4e05c920cca6`;
- evidence artifact SHA-256: `45c51df8787a32a5851ee6895d89a4c7bfc3e424364b49019f08ebe232b28845`.

See the Validation Summary Report for residual limitations and the exact final decision.

## Historical-record note

Some frozen or historical validation artifacts retain the wording used when the exercise was created. Those files are preserved because exact document identity is part of the evidence chain. Public-facing entry points use neutral demonstration language instead of rewriting frozen records after qualification.


## License

The repository code and documentation are released under the [MIT License](LICENSE).
