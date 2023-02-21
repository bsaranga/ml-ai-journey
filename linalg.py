import numpy as np
import w2_unittest

A = np.array([     
        [2, -1, 1, 1],
        [1, 2, -1, -1],
        [-1, 2, 2, 2],
        [1, -1, 2, 1]    
    ], dtype=np.dtype(int))

b = np.array([6, 3, 14, 8], dtype=np.dtype(int))

### START CODE HERE ###
# determinant of matrix A
d = np.linalg.det(A)

# solution of the system of linear equations 
# with the corresponding coefficients matrix A and free coefficients b
x = np.linalg.solve(A, b)
### END CODE HERE ###
#grade-up-to-here
#print(f"Determinant of matrix A: {d:.2f}")
#print(f"Solution vector: {x}")



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

A_test = np.array([
        [1, -2, 3, -4],
        [-5, 6, -7, 8],
        [-4, 3, -2, 1], 
        [8, -7, 6, -5]
    ], dtype=np.dtype(float))
#print("Original matrix:")
#print(A_test)

#print("\nOriginal matrix after its third row is multiplied by -2:")
#print(MultiplyRow(A_test,2,-2))

#print("\nOriginal matrix after exchange of the third row with the sum of itself and first row multiplied by 4:")
#print(AddRows(A_test,0,2,4))

#print("\nOriginal matrix after exchange of its first and third rows:")
#print(SwapRows(A_test,0,2))


def augmented_to_ref(A, b):    
    ### START CODE HERE ###
    def Stack(M, m):
        outArr = np.zeros((4,5), dtype=np.dtype(int))
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

### START CODE HERE ###

# find the value of x_4 from the last line of the reduced matrix A_ref
x_4 = 1

# find the value of x_3 from the previous row of the matrix. Use value of x_4.
x_3 = 7-3*x_4

# find the value of x_2 from the second row of the matrix. Use values of x_3 and x_4
x_2 = 22-3*x_4-4*x_3

# find the value of x_1 from the first row of the matrix. Use values of x_2, x_3 and x_4
x_1 = 3+x_4+x_3-2*x_2
### END CODE HERE ###

#print(x_1, x_2, x_3, x_4)


def ref_to_diagonal(A_ref):    
    ### START CODE HERE ###
    # multiply row 3 of the matrix A_ref by -3 and add it to the row 2
    A_diag = AddRows(A_ref, 3, 2, -3)
    
    # multiply row 3 of the new matrix A_diag by -3 and add it to the row 1
    A_diag = AddRows(A_diag, 3, 1, -3)
    
    # add row 3 of the new matrix A_diag to the row 0, replacing row 0
    A_diag = AddRows(A_diag, 3, 0, 1)
    
    # multiply row 2 of the new matrix A_diag by -4 and add it to the row 1
    A_diag = AddRows(A_diag, 2, 1, -4)
    
    # add row 2 of the new matrix A_diag to the row 0, replacing row 0
    A_diag = AddRows(A_diag, 2, 0, 1)
    
    # multiply row 1 of the new matrix A_diag by -2 and add it to the row 0
    A_diag = AddRows(A_diag, 1, 0, -2)
    ### END CODE HERE ###
    
    return A_diag
    
A_diag = ref_to_diagonal(A_ref)

#print(A_diag)
w2_unittest.test_augmented_to_ref(augmented_to_ref)