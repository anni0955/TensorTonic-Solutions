import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    ans = []
    for val in x:
        if val <= 0:
            val = np.round(lam*alpha*(np.exp(val) - 1), 4)
        else:
            val = np.round(lam*val, 4)
        
        ans.append(val)
    return ans