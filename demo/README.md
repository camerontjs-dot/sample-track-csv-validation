# SampleTrack demonstration surrogate

> **MOCK / FICTIONAL - DEMONSTRATION ONLY - NOT FOR GxP USE**

This directory contains the **custom Python/SQLite demonstration surrogate** used to exercise the frozen SampleTrack Lite OQ protocol.

It is **not** the fictional configured supplier product described by the GAMP Category 4 validation scenario.

The implementation uses only Python's standard library and SQLite so the tested behavior remains easy to inspect and reproduce.

## Development tests

```bash
python3 -m unittest discover -v
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

The authoritative final qualification was executed against exact commit `b528234a0a14db68200c9213516d0ed6a76ca56b`; see the public-release pressure qualification receipt and VSR for evidence identity and limitations.
