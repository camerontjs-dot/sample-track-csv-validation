# SampleTrack demonstration surrogate

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

This directory contains a **custom Python demonstration surrogate** built only to exercise the frozen SampleTrack Lite OQ protocol.

It is **not** the fictional configured supplier product described by the GAMP Category 4 validation scenario.

The implementation uses Python's standard library and SQLite so the qualification behavior remains easy to inspect and reproduce.

## Development test

```bash
cd demo
python -m unittest -v test_sampletrack.py
```

These unit tests are development evidence only. The frozen `STL-OQ-001` protocol remains the qualification oracle.
