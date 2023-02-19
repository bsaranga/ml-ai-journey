import numpy as np

A = np.array([     
        [2, -1, 1, 1],
        [1, 2, -1, -1],
        [-1, 2, 2, 2],
        [1, -1, 2, 1]    
    ], dtype=np.dtype(float))

b = np.array([6, 3, 14, 8], dtype=np.dtype(float))

def Stack(M, m):
    outArr = np.zeros((4,5))
    MCopy = M.copy()
    for ix, i in enumerate(m):
        outArr[ix] = np.append(MCopy[ix], i)
    return outArr

def MultiplyRow(M, row_num, row_num_multiple):
    if row_num >= 0:
        mCopy = M.copy()
        for ind, r in enumerate(mCopy[row_num]):
            mCopy[row_num][ind] = r * row_num_multiple
        return mCopy
    return M.copy()

def AddRows(M, row_num_1, row_num_2, row_num_1_multiple):
    M_new = M.copy()
    row1 = M_new[row_num_1].copy()
    row2 = M_new[row_num_2].copy()
    for ix, r in enumerate(row1):
        row2[ix] += row_num_1_multiple * r
    M_new[row_num_2] = row2
    return M_new

def SwapRows(M, row_num_1, row_num_2):
    M_new = M.copy()     
    row1 = M_new[row_num_1].copy()
    row2 = M_new[row_num_2]
    M_new[row_num_1] = row2
    M_new[row_num_2] = row1
    return M_new

def augmented_to_ref(A, b):    
    ### START CODE HERE ###
    def Stack(M, m):
        outArr = np.zeros((4,5))
        MCopy = M.copy()
        for ix, i in enumerate(m):
            outArr[ix] = np.append(MCopy[ix], i)
        return outArr
    # stack horizontally matrix A and vector b, which needs to be reshaped as a vector (4, 1)
    A_system = Stack(A, b)
    
    # swap row 0 and row 1 of matrix A_system (remember that indexing in NumPy array starts from 0)
    A_ref = SwapRows(A_system, 0, 1)
    
    # multiply row 0 of the new matrix A_ref by -2 and add it to the row 1
    A_ref = AddRows(A_ref, 0, 1, -2)
    
    # add row 0 of the new matrix A_ref to the row 2, replacing row 2
    A_ref = AddRows(A_ref, 0, 2, 1)
    
    # multiply row 0 of the new matrix A_ref by -1 and add it to the row 3
    A_ref = AddRows(A_ref, 0, 3, -1)
    
    # add row 2 of the new matrix A_ref to the row 3, replacing row 3
    A_ref = AddRows(A_ref, 2, 3, 1)
    
    # swap row 1 and 3 of the new matrix A_ref
    A_ref = SwapRows(A_ref, 1, 3)
    
    # add row 2 of the new matrix A_ref to the row 3, replacing row 3
    A_ref = AddRows(A_ref, 2, 3, 1)
    
    # multiply row 1 of the new matrix A_ref by -4 and add it to the row 2
    A_ref = AddRows(A_ref, 1, 2, -4)
    
    # add row 1 of the new matrix A_ref to the row 3, replacing row 3
    A_ref = AddRows(A_ref, 1, 3, 1)
    
    # multiply row 3 of the new matrix A_ref by 2 and add it to the row 2
    A_ref = AddRows(A_ref, 3, 2, 2)
    
    # multiply row 2 of the new matrix A_ref by -8 and add it to the row 3
    A_ref = AddRows(A_ref, 2, 3, -8)
    
    # multiply row 3 of the new matrix A_ref by -1/17
    A_ref = MultiplyRow(A_ref, 3, -1/17)
    ### END CODE HERE ###
    
    return A_ref

A_ref = augmented_to_ref(A, b)

print(A_ref)