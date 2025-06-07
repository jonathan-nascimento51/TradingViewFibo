import pytest
from fractal import add_fractal


def test_gapmin_ignores_close_prices():
    fractal_prices = []
    fractal_touches = []
    atr_value = 10.0
    vol_pct = 0.05
    atr_multiplier = 1.5

    prices = [100, 104, 108, 111]
    for price in prices:
        add_fractal(price, fractal_prices, fractal_touches, atr_value, vol_pct, atr_multiplier)

    # 104 and 108 fall inside the minimum gap so only 100 and 111 remain
    assert fractal_prices == [100, 111]
    assert fractal_touches == [0, 0]


def test_gapmin_uses_max_of_atr_and_vol():
    fractal_prices = []
    fractal_touches = []
    atr_value = 10.0
    vol_pct = 0.10  # makes vol gap bigger than ATR gap
    atr_multiplier = 1.5

    prices = [100, 110, 200]
    for price in prices:
        add_fractal(price, fractal_prices, fractal_touches, atr_value, vol_pct, atr_multiplier)

    assert fractal_prices == [100, 200]


