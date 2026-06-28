import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    g_copy = np.array(g,dtype=float).copy()
    norm = np.linalg.norm(g_copy)

    if max_norm <= 0 or norm == 0:
        return g_copy

    if norm <= max_norm:
        return g_copy

    g_clip =  g_copy * (max_norm / norm)
    return g_clip