import numpy_financial as npf

def calculate_npv(cash_flows, discount_rate=0.1):
    """
    Calculates Net Present Value (NPV)
    cash_flows: list of yearly cash flows (year 0 included)
    discount_rate: discount rate (default 10%)
    """
    npv = sum(cf / (1 + discount_rate)**i for i, cf in enumerate(cash_flows))
    return npv


def calculate_irr(cash_flows):
    """
    Calculates Internal Rate of Return (IRR)
    Uses numpy_financial.irr
    """
    return npf.irr(cash_flows)


def calculate_payback_period(cash_flows):
    """
    Calculates payback period in years.
    Returns None if investment never pays back.
    """
    cumulative = 0
    for i, cf in enumerate(cash_flows):
        cumulative += cf
        if cumulative >= 0:
            return i
    return None
