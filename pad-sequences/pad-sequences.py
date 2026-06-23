import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if seqs is None:
        return np.array(0)
    if max_len is None:
        max_len = max(len(seq) for seq in seqs)
    padded_seqs = np.full((len(seqs),max_len),pad_value)
    for i,s in enumerate(seqs):
        if len(s) > max_len:
            padded_seqs[i] = s[:max_len] 
        else:
            padded_seqs[i, :len(s)] = s  
            
    return padded_seqs