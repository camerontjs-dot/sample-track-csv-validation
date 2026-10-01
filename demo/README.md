# SampleTrack demonstration surrogate

> **MOCK / FICTIONAL - DEMONSTRATION ONLY - NOT FOR GxP USE**

This directory contains the **custom Python/SQLite demonstration surrogate** used to exercise the frozen SampleTrack Lite OQ protocol.

It is **not** the fictional configured supplier product described by the GAMP Category 4 validation scenario.

The implementation uses only Python's standard library and SQLite so the tested behavior remains easy to inspect and reproduce.

## Development tests

```bash
python3 -m unittest -v test_sampletrack.py
```

## Local OQ reproduction

```bash
python3 oq_runner.py \
  --output ../local-oq-output \
  --tester "local-reproduction" \
  --system-identity "local-working-copy" \
  --execution-id "LOCAL-OQ-001"
```

The unit tests are development evidence only. The frozen `STL-OQ-001` protocol remains the qualification authority.

The authoritative final qualification was executed against exact commit `37a23e1bb28c4fc96d6fcdc252d91e8a4e57ba0e`; see the repository-level final qualification receipt and VSR for evidence identity and limitations.
