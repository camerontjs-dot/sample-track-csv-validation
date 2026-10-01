# STL-OQ-001 — Protocol Freeze Record

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Record type | Pre-execution protocol freeze |
| Freeze status | PROTOCOL_FROZEN |
| Execution status | NOT AUTHORIZED |
| Freeze date | 2026-09-30 |
| Upstream candidate | PR #4 head `ed8d255bee0f7951710540109ec1ac9d0e23bd81` |
| Approval status | Mock approval: Not executed |

## 1. Purpose

This record freezes the **validation question, requirements, functional risk model, OQ test architecture, expected results, and test-data/configuration oracle before a demonstration system is implemented or executed against the protocol**.

The purpose is to reduce freedom to redefine successful behavior after seeing application results.

This is the first of two execution gates:

1. **PROTOCOL_FROZEN** — completed by this record.
2. **EXECUTION_READY** — not yet completed; requires an exact system-under-test identity and execution-environment prerequisites.

No OQ execution is authorized by this record alone.

## 2. Frozen authority artifacts

The following Git blob identities define this protocol freeze:

| Artifact | Frozen blob SHA |
|---|---|
| STL-SD-001 — System Description and Intended Use | `d4729f5e0f2b6151dda7b3fc73ba5adf253b8c56` |
| STL-RA-001 — Regulatory Applicability Statement | `a270ed06c54c43fe94ff4583def0de44594f5b13` |
| STL-VP-001 — Validation Plan | `6b798621cf44d8ee28c31f7dfeb267fc5ca8c491` |
| STL-URS-001 — User Requirements Specification | `673a2739bd817c5c348c94572e65e7e113766118` |
| STL-RSK-001 — Functional Risk Assessment | `0c1a36669f5ee07a219ecd358f63aa62277a1a62` |
| STL-RTM-001 — Requirements Traceability Matrix | `c653b9e8ecb55a608e55594c49649d279400ecae` |
| STL-OQ-001 — Operational Qualification Protocol | `c3e0b589362d3c12650e1ade1290da36db1a3f31` |
| STL-OQ-001 — Test Configuration and Data Set | `1f4163067d9fc35627ba4cec8253f4cbc94a60bf` |

A later file with the same filename but a different blob identity is **not** silently part of this freeze.

## 3. Frozen test architecture

The frozen protocol contains:

- 35 User Requirements;
- 15 functional risk scenarios;
- 18 OQ test cases;
- 9 High, 4 Medium, and 2 Low design-time risk classifications;
- 6 exact refrigerated temperature-boundary inputs;
- explicit role/authority rules;
- explicit material-status transitions;
- explicit electronic-signature credential behavior;
- predeclared case- and protocol-level acceptance criteria;
- deviation and re-test rules.

## 4. Mechanical pre-freeze checks

Observed before this freeze:

- OQ detailed sections: **18 / 18**
- unique OQ detailed IDs: **18 / 18**
- RTM OQ IDs resolving to protocol cases: **18 / 18**
- URS rows: **35 / 35**
- RTM URS coverage: **35 / 35**
- functional risks: **15 / 15**
- RTM risk coverage: **15 / 15**
- missing refrigerated boundary values: **0**
- step/result cells pre-populated as PASS: **0**

The six frozen REFRIGERATED_2_8C input/expected pairs are:

- 1.9 °C → Excursion
- 2.0 °C → Within range
- 2.1 °C → Within range
- 7.9 °C → Within range
- 8.0 °C → Within range
- 8.1 °C → Excursion

## 5. Source verification immediately before freeze

The OQ source interpretation was rechecked on 2026-09-30 against current official sources.

### Health Canada GUI-0050

Relevant current sections checked:

- §4.4 — validation, URS traceability, parameter/data limits, error handling;
- §4.6 — critical manual-data accuracy checks;
- §4.7 — data accessibility/readability/accuracy and backup/restore expectations;
- §4.8 — clear printouts;
- §4.9 — risk-based GMP audit trails, change/deletion reasons, intelligibility and review;
- §4.12 — authorized access, access-authorisation records, operator identity/date/time;
- §4.14 — electronic signatures, permanent record linkage, date/time.

Source:
https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/annex-11-guide-computerized-systems-gui-0050.html

### Health Canada GUI-0069

Relevant current controls checked:

- storage according to labelled/specified conditions;
- monitoring and excursion records;
- written excursion procedures;
- evidence-based accept/reject decisions;
- receiving examination and records;
- prompt transfer to proper controlled storage;
- investigation of excursions/damaged shipments.

The 2–8 °C and 15–25 °C ranges in the fixture remain **fictional test configuration**, not values claimed to come from GUI-0069.

Source:
https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/guidelines-temperature-control-drug-products-storage-transportation-0069.html

### 21 CFR Part 11 conditional overlay

The current eCFR page was checked 2026-09-30. It displayed Title 21 as up to date through 2026-09-29.

The bounded Part 11 controls exercised by this protocol include:

- §11.10(b) — accurate and complete human-readable and electronic copies;
- §11.10(d) — authorized system access;
- §11.10(e) — computer-generated time-stamped audit trail / non-obscured prior information;
- §11.10(f) — permitted sequencing;
- §11.10(g) — authority checks;
- §11.50 — signer name, date/time, meaning, and human-readable manifestation;
- §11.70 — signature/record linkage;
- §11.100(a) — unique electronic signature;
- §11.200(a)(1) — non-biometric signature components;
- §11.300(a) — uniqueness of identification-code/password combinations.

Source:
https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11

FDA Part 11 remains a **conditional exercise overlay**. This freeze does not assert FDA jurisdiction over the fictional Canadian scenario.

## 6. Source-driven repair made before freeze

The source check identified one material traceability gap before the protocol was frozen:

- URS-007 had mapped to Part 11 §11.10(b) but required only a human-readable record copy.
- §11.10(b) addresses accurate and complete copies in **both human-readable and electronic form**.

Before freeze:

- URS-007 was revised to require both forms;
- RSK-014 was updated;
- STL-RTM-001 was reconciled;
- OQ-TC-005 was expanded to verify both forms;
- signature/password mappings were narrowed to the specific Part 11 subsections actually exercised.

This correction occurred before OQ execution and before the protocol freeze. No test result was available when the acceptance boundary was changed.

## 7. What is not frozen yet

The following do not yet exist as frozen execution authority:

- runnable demonstration-surrogate commit;
- packaged/built artifact identity;
- application configuration artifact generated from the surrogate;
- execution-environment identity;
- locally provisioned mock credential identity;
- evidence manifest;
- execution timestamp.

These must be established before **EXECUTION_READY** status.

## 8. Change rule after protocol freeze

A change to any frozen artifact that can alter:

- required behavior;
- risk interpretation;
- test input;
- expected result;
- acceptance criteria;
- role authority;
- configured limit;
- traceability meaning;

creates a new protocol candidate.

Do not modify the frozen files after observing application results and continue calling the run the same experiment.

If a correction is needed before execution, create a successor freeze and state why.

If a material protocol defect is discovered during execution, preserve the affected run and handle it through the validation deviation process.

## 9. Next authorized work

The next authorized slice is **implementation of a bounded custom demonstration surrogate** from the frozen requirements/configuration, followed by:

1. exact system-under-test identity;
2. execution-readiness checks;
3. OQ execution against this frozen protocol;
4. evidence capture;
5. deviation handling without overwriting failed results.

The custom surrogate must continue to be described as a demonstration system. It does not become the fictional GAMP Category 4 supplier product.

## 10. Disposition

**PROTOCOL_FROZEN / EXECUTION NOT YET AUTHORIZED**

The protocol and test oracle are frozen strongly enough to begin implementation of the demonstration surrogate.

They do not yet establish any passing behavior.

## 11. Revision history

| Revision | Status | Description |
|---|---|---|
| 1.0 | Protocol freeze | Pre-execution validation authority frozen before system-under-test implementation/execution. |
