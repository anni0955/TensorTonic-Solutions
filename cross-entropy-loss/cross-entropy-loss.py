import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    probs = []
    for row in y_pred:
        probs.append(row[np.argmax(row)])

    probs = np.array(probs)
    log_probs = np.log(probs)

    return np.mean(-log_probs)