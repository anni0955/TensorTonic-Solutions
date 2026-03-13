import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.array(x)
    x = x/(1+np.exp(-x))
    return x