import numpy as np


def asian_option_mc(S, K, T, r, sigma, simulations, steps=100):
    dt = T / steps
    discount = np.exp(-r * T)

    payoffs = []

    for _ in range(simulations):
        prices = [S]

        for _ in range(steps):
            Z = np.random.standard_normal()
            S_next = prices[-1] * np.exp(
                (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
            )
            prices.append(S_next)

        average_price = np.mean(prices)
        payoff = max(average_price - K, 0)
        payoffs.append(payoff)

    return discount * np.mean(payoffs)