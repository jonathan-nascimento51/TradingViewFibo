# TradingViewFibo

This repository contains a Pine Script indicator and a small Python test
suite that mimics part of the indicator logic.

## Running the tests

1. Install `pytest` (for example via `pip install pytest`).
2. From the repository root, run:

```bash
pytest
```

The tests validate that the Python implementation of `addFractal` ignores
fractals that are closer than the minimum gap calculated from ATR and
volatility.
