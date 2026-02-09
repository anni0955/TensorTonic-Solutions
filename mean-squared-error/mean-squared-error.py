import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    delta_y = y_true - y_pred
    delta_y_2 = delta_y * delta_y
    return np.mean(delta_y_2)