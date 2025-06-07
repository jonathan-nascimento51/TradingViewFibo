"""Utility functions for replicating TradingView fractal logic in Python."""
from typing import List


def add_fractal(price: float,
                fractal_prices: List[float],
                fractal_touches: List[int],
                atr_value: float,
                vol_pct: float,
                atr_multiplier: float,
                max_fractals_to_check: int = 50) -> None:
    """Replicates the Pine Script `addFractal` logic.

    Parameters
    ----------
    price : float
        Price to be evaluated as a new fractal.
    fractal_prices : List[float]
        Existing fractal price list.
    fractal_touches : List[int]
        Touch counts corresponding to each fractal.
    atr_value : float
        Average True Range value.
    vol_pct : float
        Volatility percentage used to scale distance.
    atr_multiplier : float
        Multiplier applied when computing the volatility gap.
    max_fractals_to_check : int, optional
        Number of last fractals to check for duplicates, by default 50.
    """
    is_dup = False
    gap_atr = atr_value * 0.5
    gap_vol = vol_pct * price * atr_multiplier
    gap_min = max(gap_atr, gap_vol)

    start_idx = max(0, len(fractal_prices) - max_fractals_to_check)
    for fp in fractal_prices[start_idx:]:
        if abs(price - fp) < gap_min:
            is_dup = True
            break

    if not is_dup:
        fractal_prices.append(price)
        fractal_touches.append(0)
