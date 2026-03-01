import numpy as np
import matplotlib.pyplot as plt

from monte_carlo.variance_reduction import (
    mc_standard,
    mc_antithetic,
    mc_control_variate,
)

from monte_carlo.asian import asian_option_mc
from monte_carlo.barrier import up_and_out_call_mc
from models.black_scholes import black_scholes_price
from greeks.finite_difference import delta_mc, gamma_mc, vega_mc


# =============================
# Market Parameters
# =============================
S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2
barrier = 130


# =============================
# Simulation Setup
# =============================
simulations_list = np.linspace(1000, 50000, 30)

std_errors = []
anti_errors = []
control_errors = []

bs_price = black_scholes_price(S, K, T, r, sigma)


# =============================
# Run Variance Reduction Experiment
# =============================
for sims in simulations_list:
    sims = int(sims)

    price_std = mc_standard(S, K, T, r, sigma, sims)
    price_anti = mc_antithetic(S, K, T, r, sigma, sims)
    price_control = mc_control_variate(S, K, T, r, sigma, sims)

    std_errors.append(abs(price_std - bs_price))
    anti_errors.append(abs(price_anti - bs_price))
    control_errors.append(abs(price_control - bs_price))


# =============================
# Plot Variance Reduction
# =============================
plt.figure(figsize=(10, 6))
plt.plot(simulations_list, std_errors, label="Standard MC")
plt.plot(simulations_list, anti_errors, label="Antithetic")
plt.plot(simulations_list, control_errors, label="Control Variate")

plt.xlabel("Simulations")
plt.ylabel("Absolute Error")
plt.title("Variance Reduction Comparison")
plt.legend()
plt.grid(True)
plt.show()


# =============================
# Asian Option Pricing
# =============================
asian_price = asian_option_mc(S, K, T, r, sigma, simulations=20000)


# =============================
# Barrier Option Pricing
# =============================
barrier_price = up_and_out_call_mc(
    S, K, barrier, T, r, sigma, simulations=20000
)


# =============================
# Greeks via Monte Carlo
# =============================
delta_est = delta_mc(S, K, T, r, sigma, simulations=30000)
gamma_est = gamma_mc(S, K, T, r, sigma, simulations=30000)
vega_est = vega_mc(S, K, T, r, sigma, simulations=30000)


# =============================
# Final Output
# =============================
print("\n===== PRICING RESULTS =====")
print("Black-Scholes Price:", bs_price)
print("Asian Option Price (MC):", asian_price)
print("Up-and-Out Barrier Call Price:", barrier_price)

print("\n===== MONTE CARLO GREEKS =====")
print("Delta:", delta_est)
print("Gamma:", gamma_est)
print("Vega:", vega_est)