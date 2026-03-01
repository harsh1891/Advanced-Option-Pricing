import numpy as np
from monte_carlo.variance_reduction import mc_standard


def delta_mc(S, K, T, r, sigma, simulations, h=0.1):
    price_up = mc_standard(S + h, K, T, r, sigma, simulations)
    price_down = mc_standard(S - h, K, T, r, sigma, simulations)
    return (price_up - price_down) / (2 * h)


def gamma_mc(S, K, T, r, sigma, simulations, h=0.1):
    price_up = mc_standard(S + h, K, T, r, sigma, simulations)
    price_mid = mc_standard(S, K, T, r, sigma, simulations)
    price_down = mc_standard(S - h, K, T, r, sigma, simulations)
    return (price_up - 2 * price_mid + price_down) / (h ** 2)


def vega_mc(S, K, T, r, sigma, simulations, h=0.01):
    price_up = mc_standard(S, K, T, r, sigma + h, simulations)
    price_down = mc_standard(S, K, T, r, sigma - h, simulations)
    return (price_up - price_down) / (2 * h)