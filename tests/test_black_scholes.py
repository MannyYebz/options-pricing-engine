import pytest
from models.black_scholes import black_scholes, greeks

# Known inputs we'll reuse across all tests
S, K, T, r, sigma = 150, 150, 0.25, 0.05, 0.2

def test_call_price_positive():
    price = black_scholes(S, K, T, r, sigma, option_type="call")
    assert price > 0

def test_put_price_positive():
    price = black_scholes(S, K, T, r, sigma, option_type="put")
    assert price > 0

def test_call_price_accuracy():
    price = black_scholes(S, K, T, r, sigma, option_type="call")
    assert abs(price - 6.92) < 0.01

def test_higher_stock_price_increases_call():
    price_low  = black_scholes(100, K, T, r, sigma, option_type="call")
    price_high = black_scholes(200, K, T, r, sigma, option_type="call")
    assert price_high > price_low

def test_higher_stock_price_decreases_put():
    price_low  = black_scholes(100, K, T, r, sigma, option_type="put")
    price_high = black_scholes(200, K, T, r, sigma, option_type="put")
    assert price_high < price_low

def test_invalid_option_type_raises_error():
    with pytest.raises(ValueError):
        black_scholes(S, K, T, r, sigma, option_type="invalid")

def test_delta_call_between_0_and_1():
    result = greeks(S, K, T, r, sigma, option_type="call")
    assert 0 < result["delta"] < 1

def test_delta_put_between_minus1_and_0():
    result = greeks(S, K, T, r, sigma, option_type="put")
    assert -1 < result["delta"] < 0

def test_gamma_positive():
    result = greeks(S, K, T, r, sigma, option_type="call")
    assert result["gamma"] > 0

def test_theta_negative():
    result = greeks(S, K, T, r, sigma, option_type="call")
    assert result["theta"] < 0