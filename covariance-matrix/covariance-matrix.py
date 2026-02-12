import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.array(X)
    if X.shape[0] == 1 or X.ndim == 1: 
        return None
    
    return np.atleast_2d(np.cov(X.T))