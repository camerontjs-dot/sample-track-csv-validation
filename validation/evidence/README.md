# OQ Evidence Directory

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

No executed OQ evidence exists yet.

When execution begins, store evidence under test-scoped paths where practical, for example:

```text
evidence/
  OQ-TC-001/
    STL-EV-OQ-001-01-...
  OQ-TC-002/
    STL-EV-OQ-002-01-...
```

## Evidence rules

- use stable evidence IDs;
- identify the test/execution the evidence belongs to;
- preserve original failed-run evidence after repair/re-test;
- do not overwrite one execution with another;
- avoid real patient, customer, employee, supplier, or production data;
- do not commit passwords, tokens, or other credentials;
- capture only evidence needed to establish the decision-relevant result;
- when checksums are generated later, treat them as evidence-object identity/integrity controls rather than proof that the tested behavior is correct.

The future evidence manifest should record, where useful:

`evidence ID | test ID | execution ID | filename | SHA-256 | capture time | system-under-test identity`
