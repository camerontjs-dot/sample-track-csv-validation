# OQ Evidence Directory

> **MOCK / FICTIONAL - DEMONSTRATION ONLY - NOT FOR GxP USE**

This directory contains durable repository-facing receipts for executed SampleTrack Lite mock OQ runs.

## Current release authority

- [OQ-CI-36897449285 receipt](OQ-CI-36897449285/README.md)
- [OQ-CI-36897449285 step-level execution](OQ-CI-36897449285/execution.md)
- [OQ-CI-36897449285 evidence-object manifest](OQ-CI-36897449285/manifest.json)

Current successor result:

- development/adversarial pressure suite: **18 / 18 PASS**
- unchanged frozen OQ: **18 / 18 PASS**
- exact application/runner candidate: `b528234a0a14db68200c9213516d0ed6a76ca56b`

## Preserved historical execution

The earlier bounded qualification remains available as historical evidence:

- [OQ-CI-36813357212 receipt](OQ-CI-36813357212/README.md)
- [OQ-CI-36813357212 step-level execution](OQ-CI-36813357212/execution.md)

Earlier failed and partially sufficient executions are documented in `STL-DL-001` and GitHub Actions history rather than being rewritten out of the record.

## Evidence rules

- use stable evidence IDs and execution IDs;
- identify the exact system-under-test source;
- preserve failed evidence after repair/retest;
- do not overwrite one execution with another;
- do not commit real regulated, patient, customer, employee, supplier, or production data;
- do not commit passwords, tokens, or other credentials;
- preserve checksums as evidence-object identity/integrity controls, not as proof that the behavior is correct.

The GitHub Actions artifact ZIP remains the byte-exact generated-bundle authority where referenced. Repository copies provide durable, readable evidence and hash ledgers beyond Actions retention.
