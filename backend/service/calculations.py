import numpy as np
import numpy_financial as nf

def calculate_irr(cashflows):
    return nf.irr(cashflows)
