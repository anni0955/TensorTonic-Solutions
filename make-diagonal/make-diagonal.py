import numpy as np
def withLoop(v):
    n = len(v)
    ans = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            if i == j:
                ans[i][j] = v[i]

    return ans 
def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    return withLoop(v)