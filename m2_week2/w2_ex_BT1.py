import numpy as np
# cau 1 a: do dai cua vector


def compute_vector_length(vector):    
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector
# cau 1b: tinh tich vo huong


def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result
# cau 1c: nhan c voi ma tran


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result
# cau 1d: nhan ma tran voi ma tran


def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result
# cau 1e: tim ma tran nghich dao


def inverse_matrix(matrix):
    det_matrix = np.linalg.det(matrix)
    if det_matrix != 0:
        result = np.linalg.inv(matrix)
    else:
        result = None
    return result


if __name__ == '__main__':
    v = np.array([4, 3])
    u = np.array([1, 2])
    a = np.array([[1, 2], [3, 4]])
    print(f'vector v: \n{v}')
    print(f'vector v: \n{u}')
    print(f'matrix: \n{a}')
    print(f'Cau 1 a, length of vector: {compute_vector_length(v)}')
    print('Cau 1 b: tich vo huong cua vector va vector:')
    print(compute_dot_product(u, v))
    print(f'Cau 1 c: nhan vector voi ma tran:\n{matrix_multi_vector(a, v)}')
    print(f'Cau 1 d: nhan ma tran voi ma tran:\n{matrix_multi_matrix(a, a)}')
    print(f'Cau 1 e: ma tran nghich dao :\n{inverse_matrix(a)}')
