import numpy as np

def monte_carlo_simulation(data, simulations=1000):
    returns = np.diff(data) / data[:-1]
    mean = np.mean(returns)
    std = np.std(returns)

    results = []
    for _ in range(simulations):
        simulated = np.random.normal(mean, std)
        results.append(simulated)

    return {
        "mean_return": float(mean),
        "std_dev": float(std),
        "simulated_avg": float(np.mean(results))
    }
