import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    indices = np.argmax(y_pred, axis=1)

    probs = y_pred[np.arange(y_pred.shape[0]), indices]
    log_probs = np.log(probs)

    return np.mean(-log_probs)