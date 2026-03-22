import numpy as np

def monte_carlo(S, K, T, r, sigma, simulations=10000, option_type="call"):
    """
    Price a European option using Monte Carlo simulation.

    Parameters:
        S           : Current stock price
        K           : Strike price
        T           : Time to expiration in years
        r           : Risk-free interest rate
        sigma       : Volatility of the stock
        simulations : Number of simulations to run
        option_type : "call" or "put"
    """
    # Step 1: Generate random numbers
    Z = np.random.standard_normal(simulations)

    # Step 2: Simulate final stock prices
    ST = S * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * Z)

    # Step 3: Calculate payoffs
    if option_type == "call":
        payoffs = np.maximum(ST - K, 0)
    elif option_type == "put":
        payoffs = np.maximum(K - ST, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    # Step 4: Discount and average
    price = np.exp(-r * T) * np.mean(payoffs)

    return round(price, 4)