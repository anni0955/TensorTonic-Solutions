import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.array(x, ndmin=1)
    ans = (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))
    return ans