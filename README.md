# Sample Track CSV Validation

> **MOCK / FICTIONAL - DEMONSTRATION ONLY - NOT FOR GxP USE**

## One-page summary

I built this to show how I would validate a GxP computerized system end to end, at a size one person can actually check. The system is fictional. The execution evidence is real: every pass and every failure below came from a GitHub Actions run against an exact commit.

The hard part was not getting to 18 / 18. It was keeping the earlier failures, like the 8.0 °C boundary defect (DEV-001) and the forgeable session (DEV-004), on the record after they were fixed.

### What I built

- A mock validation package for SampleTrack Lite, a fictional sample and inventory tracker in a pharmaceutical warehouse scenario: intended use (STL-SD-001), regulatory applicability (STL-RA-001), validation plan (STL-VP-001), 35 user requirements (STL-URS-001), 15 functional risks (STL-RSK-001), an 18-case OQ protocol (STL-OQ-001), a traceability matrix (STL-RTM-001), a deviation log (STL-DL-001), and a summary report (STL-VSR-001).
- A small Python and SQLite demonstration surrogate (`demo/sampletrack.py`), an automated OQ runner (`demo/oq_runner.py`), and 20 development and adversarial tests.
- A CI workflow (`.github/workflows/sampletrack-oq.yml`) that stops unless six frozen validation artifacts (five documents and the test configuration) still match their pinned Git blob hashes, then compiles, runs the tests, runs the frozen OQ once, and keeps the evidence with SHA-256 digests.

### What I own

This is a single-owner exercise. Every commit in the history is under my GitHub account, and the scenario, requirement, risk, freeze, and deviation decisions recorded here are mine. Because I also built the surrogate and the runner, the OQ is reproducible behavioral evidence, not independent validation. The VSR says the same thing in section 7.

### What it shows

- Writing testable requirements and tracing them both ways: 35 URS to 15 risks to 18 OQ cases.
- FMEA-style risk scoring with explicit severity overrides, and keeping the design-time scores unchanged after testing instead of lowering them after a pass.
- Freezing the protocol and expected results before execution, then fixing the system or the test apparatus, not the expected results, when a run failed.
- Deviation handling: each finding classified, corrected, and retested or reconciled, with the failed runs preserved.
- Mapping controls to Health Canada GUI-0050 and GUI-0069, with selected 21 CFR Part 11 controls as a conditional overlay only.
- Using CI as the qualification apparatus: hash-pinned inputs, exact-commit checkout, and an evidence manifest per run.

### Headline numbers

Taken from STL-RTM-001 (section 4) and STL-VSR-001 (sections 9, 11 and 12):

- URS traceability: 35 / 35 VERIFIED - PASS
- functional risks: 15 (9 High, 4 Medium, 2 Low), each with at least one executed OQ path
- frozen OQ: 18 / 18 PASS on candidate `c3463a18`, execution `OQ-CI-36947930824`
- development and adversarial tests: 20 / 20 PASS
- recorded validation deviations: 13 / 13 resolved, 0 open

### Limits

Everything here is mock. There is no production IQ or PQ, no supplier qualification, no real QA approval, and no claim of regulatory compliance. The approval blocks in the package are deliberately unsigned. The final disposition is ACCEPTED FOR BOUNDED MOCK DEMONSTRATION USE and NOT APPROVED FOR GxP PRODUCTION USE.

## Repository overview

This repository is a bounded computerized system validation (CSV) exercise for **SampleTrack Lite**, a fictional sample and inventory tracking system in a pharmaceutical warehouse/distribution scenario.

It follows one validation thread from intended use through requirements, risk, frozen qualification, observed failures, controlled correction, traceability closure, and a final bounded decision.

It does **not** establish production validation, regulatory compliance, supplier qualification, or suitability for real GxP use.

## Current bounded result

Exact qualified custom demonstration surrogate:

`c3463a18b18c359d4d639055c4e3f6121df79f80`

Final qualification evidence:

- development and adversarial pressure tests: **20 / 20 PASS**;
- frozen OQ: **18 / 18 PASS**;
- URS traceability: **35 / 35 VERIFIED - PASS**;
- recorded validation deviations: **13 / 13 resolved**;
- final mock disposition: **ACCEPTED FOR BOUNDED MOCK DEMONSTRATION USE**;
- production disposition: **NOT APPROVED FOR GxP PRODUCTION USE**.

The passing final run does not replace the failed executions that preceded it. The failure and correction lineage remains part of the validation record.

## What the pressure test added

A separate pre-publication adversarial pass challenged behaviors beyond the original OQ examples. It found additional defects in stale verification state, status-change rationale, regulated read authorization, authentication ordering, malformed temperature handling, and one qualification-role mismatch.

Those findings were preserved as DEV-005 through DEV-010. A final source-to-URS pass then found DEV-011: receiving could complete without the distinct receipt date required by URS-002. Publication remained blocked until the corrected receipt-date successor passed 19 pressure tests and the unchanged OQ. A final requirement-level challenge then exposed DEV-012: denied completed-record deletion attempts were not audited. The terminal successor passed the expanded 20-test pressure suite and the unchanged 18-case frozen OQ. After that, DEV-013 corrected how the repository copy of the terminal evidence matched the hosted run (restored hosted-original bytes and corrected provenance pointers) without changing the candidate or the result.

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
- [Current step-level OQ execution record](validation/evidence/OQ-CI-36947930824/execution.md)
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

- run: `36947930824`;
- execution ID: `OQ-CI-36947930824`;
- exact qualified commit: `c3463a18b18c359d4d639055c4e3f6121df79f80`;
- evidence artifact SHA-256: `0ac0db89702f40c98204f65537e23950b04fb3b5348bc0c11d03ca54f4315749`.

See the Validation Summary Report for residual limitations and the exact final decision.

## Historical-record note

Some frozen or historical validation artifacts retain the wording used when the exercise was created. Those files are preserved because exact document identity is part of the evidence chain. Public-facing entry points use neutral demonstration language instead of rewriting frozen records after qualification.


## License

The repository code and documentation are released under the [MIT License](LICENSE).
