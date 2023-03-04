import numpy as np

# #columns of mat1 must be equal to the #rows of mat2 in order to multiply
mat1 = np.array([[2,6,4],[4,1,7],[8,4,9]])
mat2 = np.array([[2,2],[3,3],[4,4]])

try:
    mult = np.matmul(mat1,mat2)
except ValueError as err:
    print(err)

mat3 = np.array([[1,2,-1],[1,0,1],[0,1,0]])
det_mat3 = np.linalg.det(mat3)
inv_mat3 = np.linalg.inv(mat3)
id_mat = np.array([[1,0,0],[0,1,0],[0,0,1]])
id_mat_rank = np.linalg.matrix_rank(id_mat)

vec_b = np.array([5,-2,0])

matA = np.array([[5,2,3],[-1,-3,2],[0,1,-1]])
matB = np.array([[1,0,-4],[2,1,0],[8,-1,0]])
matAB = matA @ matB