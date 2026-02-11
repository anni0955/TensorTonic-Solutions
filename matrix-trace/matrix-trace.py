import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A = np.array(A)
    ans = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i == j:
                ans += A[i][j]

    return ans