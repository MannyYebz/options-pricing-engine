# Options Pricing Engine

A Python-based options pricing engine implementing three quantitative finance models from scratch. Built as a portfolio project to demonstrate practical knowledge of derivatives pricing, financial mathematics, and software engineering.

---

## Models Implemented

### Black-Scholes Model
Closed-form analytical solution for pricing European options.
- Call and Put pricing
- Full Greeks calculation (Delta, Gamma, Vega, Theta, Rho)

### Binomial Tree Model
Discrete-time lattice model for pricing both European and American options.
- Configurable number of time steps
- Supports early exercise (American options)
- Converges to Black-Scholes as steps increase

### Monte Carlo Simulation
*(Coming soon)*
- Simulates thousands of possible stock price paths
- Estimates option price from average payoff

---

## Project Structure
```
options-pricing-engine/
│
├── models/
│   ├── black_scholes.py      # Black-Scholes pricing + Greeks
│   ├── binomial_tree.py      # Binomial Tree pricing
│   └── monte_carlo.py        # Monte Carlo simulation
│
├── tests/
│   └── test_black_scholes.py # Unit tests
│
├── notebooks/                # Jupyter walkthroughs (coming soon)
├── requirements.txt
└── README.md
```

---

## Quickstart

**1. Clone the repository**
```bash
git clone https://github.com/MannyYebz/options-pricing-engine.git
cd options-pricing-engine
```

**2. Create and activate virtual environment**
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate       # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## Usage Examples

### Black-Scholes Pricing
```python
from models.black_scholes import black_scholes

price = black_scholes(S=150, K=150, T=0.25, r=0.05, sigma=0.2, option_type="call")
print(f"Call Price: ${price}")
# Output: Call Price: $6.92
```

### Greeks
```python
from models.black_scholes import greeks

result = greeks(S=150, K=150, T=0.25, r=0.05, sigma=0.2, option_type="call")
print(result)
# Output: {'delta': 0.5695, 'gamma': 0.0262, 'vega': 0.2947, 'theta': -0.043, 'rho': 0.1962}
```

### Binomial Tree
```python
from models.binomial_tree import binomial_tree

# European Call
price = binomial_tree(S=150, K=150, T=0.25, r=0.05, sigma=0.2, steps=100, option_type="call", option_style="european")
print(f"European Call: ${price}")
# Output: European Call: $6.9075

# American Put
price = binomial_tree(S=150, K=150, T=0.25, r=0.05, sigma=0.2, steps=100, option_type="put", option_style="american")
print(f"American Put: ${price}")
# Output: American Put: $5.2119
```

---

## Parameter Reference

| Parameter | Description | Example |
|---|---|---|
| `S` | Current stock price | `150` |
| `K` | Strike price | `150` |
| `T` | Time to expiration (years) | `0.25` (3 months) |
| `r` | Risk-free interest rate | `0.05` (5%) |
| `sigma` | Annualized volatility | `0.2` (20%) |
| `option_type` | Call or put | `"call"` |
| `option_style` | European or American | `"european"` |
| `steps` | Binomial tree steps | `100` |

---

## Tech Stack

- **Python 3.14**
- **NumPy** — numerical computations
- **SciPy** — normal distribution functions
- **Matplotlib** — visualizations (coming soon)
- **Pandas** — data handling (coming soon)
- **Jupyter** — interactive notebooks (coming soon)

---

## Author

**Emmanuel** — aspiring Quantitative Analyst
- GitHub: [@MannyYebz](https://github.com/MannyYebz)

---

*This project is for educational and portfolio purposes.*