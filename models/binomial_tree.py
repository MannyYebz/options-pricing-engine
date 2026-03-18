import numpy as np

def binomial_tree(S, K, T, r, sigma, steps, option_type="call", option_style="european"):
    """
    Price a European or American option using the Binomial Tree model.

    Parameters:
        S            : Current stock price
        K            : Strike price
        T            : Time to expiration in years
        r            : Risk-free interest rate
        sigma        : Volatility of the stock
        steps        : Number of time steps in the tree
        option_type  : "call" or "put"
        option_style : "european" or "american"
    """
    dt       = T / steps
    u        = np.exp(sigma * np.sqrt(dt))
    d        = 1 / u
    p        = (np.exp(r * dt) - d) / (u - d)
    discount = np.exp(-r * dt)

    # Step 1: Build stock price tree at expiration
    stock_prices = np.zeros(steps + 1)
    for i in range(steps + 1):
        stock_prices[i] = S * (u ** (steps - i)) * (d ** i)

    # Step 2: Calculate option values at expiration
    option_values = np.zeros(steps + 1)
    for i in range(steps + 1):
        if option_type == "call":
            option_values[i] = max(stock_prices[i] - K, 0)
        elif option_type == "put":
            option_values[i] = max(K - stock_prices[i], 0)

    # Step 3: Work backwards through the tree
    for step in range(steps - 1, -1, -1):
        for i in range(step + 1):
            hold = discount * (p * option_values[i] + (1 - p) * option_values[i + 1])

            if option_style == "american":
                if option_type == "call":
                    exercise = S * (u ** (step - i)) * (d ** i) - K
                elif option_type == "put":
                    exercise = K - S * (u ** (step - i)) * (d ** i)
                option_values[i] = max(hold, exercise)
            else:
                option_values[i] = hold

    return round(option_values[0], 4)