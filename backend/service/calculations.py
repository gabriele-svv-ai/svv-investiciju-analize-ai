import numpy as np

def calculate_npv(cash_flows, discount_rate=0.1):
    npv = sum(cf / (1 + discount_rate)**i for i, cf in enumerate(cash_flows))
    return npv

def calculate_irr(cash_flows):
    return np.irr(cash_flows)
