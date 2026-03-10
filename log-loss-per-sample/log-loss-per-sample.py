import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    
    n = len(y_true)
    ans = []
    for i in range(n):
        if y_pred[i] > 1-1e-15:
            y_pred[i] = 1-1e-15
        elif y_pred[i] < 1e-15:
            y_pred[i] = 1e-15
            
        loss = -(y_true[i]*math.log(y_pred[i]) + (1-y_true[i])*math.log(1-y_pred[i]))
        ans.append(loss)

    return ans
        
        