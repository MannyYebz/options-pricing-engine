import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    Calculate the Black-Scholes option price.

    Parameters:
    S : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to maturity (in years)
    r : float
        Risk-free interest rate (annualized)
    sigma : float
        Volatility of the underlying stock (annualized)
    option_type : str
        Type of the option ('call' or 'put')

    Returns:
    float
        Theoretical price of the option
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price


def greeks(S, K, T, r, sigma, option_type="call"):
    """
    Calculate the Greeks for a European option.

    Parameters:
        S     : Current stock price
        K     : Strike price
        T     : Time to expiration in years
        r     : Risk-free interest rate
        sigma : Volatility of the stock
        option_type : "call" or "put"

    Returns:
        dict of Greeks: delta, gamma, vega, theta, rho
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega  = S * norm.pdf(d1) * np.sqrt(T) * 0.01

    if option_type == "call":
        delta = norm.cdf(d1)
        theta = (-(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
                - r * K * np.exp(-r * T) * norm.cdf(d2)) / 365
        rho   = K * T * np.exp(-r * T) * norm.cdf(d2) * 0.01
    elif option_type == "put":
        delta = norm.cdf(d1) - 1
        theta = (-(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
                + r * K * np.exp(-r * T) * norm.cdf(-d2)) / 365
        rho   = -K * T * np.exp(-r * T) * norm.cdf(-d2) * 0.01
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return {
        "delta": round(delta, 4),
        "gamma": round(gamma, 4),
        "vega" : round(vega,  4),
        "theta": round(theta, 4),
        "rho"  : round(rho,   4)
    }