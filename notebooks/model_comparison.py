import sys
sys.path.insert(0, ".")

import numpy as np
import matplotlib.pyplot as plt
from models.black_scholes import black_scholes
from models.binomial_tree import binomial_tree
from models.monte_carlo import monte_carlo

# Fixed parameters
K     = 150
T     = 0.25
r     = 0.05
sigma = 0.2

# Range of stock prices to plot
stock_prices = np.linspace(100, 200, 50)

# Calculate prices for each model across all stock prices
bs_calls  = [black_scholes(S, K, T, r, sigma, "call") for S in stock_prices]
bt_calls  = [binomial_tree(S, K, T, r, sigma, 100, "call", "european") for S in stock_prices]
mc_calls  = [monte_carlo(S, K, T, r, sigma, 10000, "call") for S in stock_prices]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(stock_prices, bs_calls, label="Black-Scholes", linewidth=2)
plt.plot(stock_prices, bt_calls, label="Binomial Tree", linewidth=2, linestyle="--")
plt.plot(stock_prices, mc_calls, label="Monte Carlo",   linewidth=2, linestyle=":")

plt.axvline(x=K, color="gray", linestyle="--", alpha=0.5, label="Strike Price")
plt.title("Call Option Price Comparison Across Models", fontsize=14)
plt.xlabel("Stock Price ($)")
plt.ylabel("Option Price ($)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("notebooks/model_comparison.png", dpi=150)
plt.show()
print("Chart saved to notebooks/model_comparison.png")