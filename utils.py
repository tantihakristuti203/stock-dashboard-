import numpy as np

def scoring(r, v, b):
    if r > 0.5 and v < 0.25 and (not np.isnan(b) and b <= 1.5):
        return "Overperform / Low Risk"
    elif r > 0 and v < 0.35:
        return "Moderate"
    else:
        return "Underperform / High Risk"
