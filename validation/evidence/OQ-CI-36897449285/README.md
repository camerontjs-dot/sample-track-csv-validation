# OQ-CI-36897449285 — Public-release pressure qualification

> **MOCK / FICTIONAL — DEMONSTRATION ONLY — NOT FOR GxP USE**

This directory preserves the final successor qualification record produced after the public-release pressure test.

## Exact identity

- candidate: `b528234a0a14db68200c9213516d0ed6a76ca56b`
- tree: `834831c3df75d2a610c338c02657036c8ee9695a`
- GitHub Actions run: `36897449285`
- job: `110487913996`
- execution ID: `OQ-CI-36897449285`
- environment: Ubuntu 24.04 / x86_64 / Python 3.13.15 / SQLite 3.45.1

## Result

- compilation: **PASS**
- development + adversarial pressure tests: **18 / 18 PASS**
- unchanged frozen OQ: **18 / 18 PASS**
- OQ failures: **0**

## Source SHA-256

- `demo/sampletrack.py`: `c719094618123bc280cb0d9ce204da1f7072004e40e48a9787b38b02f1aa14b5`
- `demo/test_sampletrack.py`: `1a9a45f3710b452b9b078d738698011b21d964f4803e97b510afe410f1484363`
- `demo/oq_runner.py`: `aac407bec114b285298642f4ae22f8fa8d32d384e5cd170542073687689ea5b6`

## Core execution SHA-256

- `execution.json`: `1ccd18f02deaf920f08f2742906a37e70d375e6b0f7f3f87c13e39df774e2b3b`
- `execution.md`: `6129581178cad83cd9fadf64a20795ea4128e73d220794c78dd9358b8fad55d7`
- `manifest.json`: `2f572bad3c11ea34a2c343da5dee839b602874c14ce36c9bbee3772f56df1e08`

## GitHub Actions artifact

- artifact ID: `11180665087`
- artifact name: `sampletrack-oq-36897449285`
- ZIP SHA-256: `7c1d8c52dd6161b16130d20699ce1a5ff47a4edc9ef54454cd469966af6c05af`
- size: 25,925 bytes

The downloaded ZIP was independently hashed after retrieval and matched GitHub's reported digest. `unzip -t` reported no compressed-data errors.

The repository preserves the readable execution record and the original evidence-object SHA-256 manifest. The workflow artifact is the byte-exact authority for the original generated bundle.

## Pressure-test lineage

The final pass follows preserved failures in the same PR:

- run `36895767954`: four requirement-level failures, frozen OQ not entered;
- run `36896153123`: first-wave corrections passed 16/16 tests and 18/18 OQ;
- run `36897292169`: second sweep exposed non-finite/malformed temperature handling; frozen OQ not entered;
- run `36897449285`: all 18 development/adversarial tests and all 18 frozen OQ cases passed.

See `STL-DL-001-validation-deviation-log.md` for DEV-005 through DEV-010.
