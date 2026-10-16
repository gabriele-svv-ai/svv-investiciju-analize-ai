from .finance_api import get_stock_data
from .calculations import calculate_npv, calculate_irr
from .monte_carlo import monte_carlo_simulation

def analyze_investment(symbol):
    data = get_stock_data(symbol)

    mc = monte_carlo_simulation(data)
    irr = calculate_irr(data)
    npv = calculate_npv(data)

    return {
        "symbol": symbol,
        "npv": npv,
        "irr": irr,
        "monte_carlo": mc
    }
