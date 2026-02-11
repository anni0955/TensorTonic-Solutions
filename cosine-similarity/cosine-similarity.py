import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.array(a)
    b = np.array(b)
    if a.shape != b.shape:
        return 0
    nume = np.dot(a, b)
    deno = np.sqrt(np.dot(a, a)) * np.sqrt(np.dot(b, b))
    if deno == 0:
        return 0
    return nume/deno