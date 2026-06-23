import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    if x is None:
        return 
    x = np.array(x)
    return 1 /( 1 + np.exp(-x))