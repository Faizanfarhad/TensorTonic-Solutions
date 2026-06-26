import math
import numpy as np 
def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    
    y_true = np.array(y_true)
    for pred in range(len(y_pred)):
        if y_pred[pred]> 1-eps:
            y_pred[pred] = 1-eps
        elif y_pred[pred] < eps:
            y_pred[pred] = eps 
    
    y_pred = np.array(y_pred)
    fir = y_true * np.log(y_pred)
    sec = 1 - y_true
    thi = np.log(1-y_pred)

    loss = -(fir + sec * thi)
    loss = loss.tolist()
    return loss