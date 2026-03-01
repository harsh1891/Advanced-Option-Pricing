import numpy as np
from models.black_scholes import black_scholes_price

def mc_standard(S, K, T, r, sigma, simulations):
    Z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
    payoff = np.maximum(ST - K, 0)
    return np.exp(-r*T) * np.mean(payoff)


def mc_antithetic(S, K, T, r, sigma, simulations):
    Z = np.random.standard_normal(simulations//2)
    Z_full = np.concatenate([Z, -Z])
    ST = S * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z_full)
    payoff = np.maximum(ST - K, 0)
    return np.exp(-r*T) * np.mean(payoff)


def mc_control_variate(S, K, T, r, sigma, simulations):
    Z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)

    payoff_mc = np.maximum(ST - K, 0)
    discounted_mc = np.exp(-r*T) * payoff_mc

    bs_exact = black_scholes_price(S, K, T, r, sigma)

    # control variate adjustment
    control = ST
    expected_control = S * np.exp(r*T)

    beta = np.cov(discounted_mc, control)[0,1] / np.var(control)

    adjusted = discounted_mc - beta * (control - expected_control)
    return np.mean(adjusted)