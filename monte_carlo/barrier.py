import numpy as np

def up_and_out_call_mc(S, K, B, T, r, sigma, simulations, steps=100):
    dt = T / steps
    discount = np.exp(-r * T)

    payoffs = []

    for _ in range(simulations):
        price = S
        knocked_out = False

        for _ in range(steps):
            Z = np.random.standard_normal()
            price = price * np.exp(
                (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
            )

            if price >= B:
                knocked_out = True
                break

        if not knocked_out:
            payoffs.append(max(price - K, 0))
        else:
            payoffs.append(0)

    return discount * np.mean(payoffs)