from .calculations import calculate_npv, calculate_irr, calculate_payback_period
from .monte_carlo import monte_carlo_simulation

def analyze_svv_project(initial_investment, yearly_cash_flows, discount_rate=0.1):
    """
    SVV investicijų analizė:
    - initial_investment: neigiamas skaičius, pvz. -50000
    - yearly_cash_flows: sąrašas metinių pinigų srautų, pvz. [12000, 15000, 18000]
    - discount_rate: diskonto norma (default 10%)
    """

    # Sukuriame cash flow masyvą: investicija + metiniai srautai
    cash_flows = [initial_investment] + yearly_cash_flows

    npv = calculate_npv(cash_flows, discount_rate)
    irr = calculate_irr(cash_flows)
    payback = calculate_payback_period(cash_flows)

    # Monte Carlo rizikos analizė
    mc = monte_carlo_simulation(yearly_cash_flows)

    return {
        "initial_investment": initial_investment,
        "cash_flows": yearly_cash_flows,
        "npv": npv,
        "irr": irr,
        "payback_period": payback,
        "monte_carlo": mc
    }
