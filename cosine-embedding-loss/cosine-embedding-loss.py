import numpy as np 
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    cos = np.dot(x1, x2)/(np.sqrt(np.dot(x1, x1))*np.sqrt(np.dot(x2, x2)))
    if label == 1: 
        return (1 - cos)
    else:
        return max(0, cos-margin)
        
        