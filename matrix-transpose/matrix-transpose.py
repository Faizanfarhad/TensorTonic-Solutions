import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    '''
    transpose = [[row[col] for row in A] for col in range(A[0])]
    transpose = np.array(transpose)''' #Not worked due to an 
    transpose = np.array(A).T
    return transpose
