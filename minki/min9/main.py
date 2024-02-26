def base_matrix_multiply(matrix1, matrix2):
    """
    O(m*n*o)
    o, m, n size of matr
    """
    matrix1_len1 = len(matrix1)
    matrix2_len1 = len(matrix2)
    matrix2_len2 = len(matrix2[0])

    res = [[0 for _ in range(matrix2_len2)] for _ in range(matrix1_len1)]

    for i in range(matrix1_len1):
        for j in range(matrix2_len2):
            for m in range(matrix2_len1):
                res[i][j] += matrix1[i][m] * matrix2[m][j]
    return res


def matrix_size_normalize(matrix, size):
    '''
    O(size^2)
    '''
    res = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res[i][j] = matrix[i][j]
    return res


def split_for_matrix(matrix, size):
    a = [matrix[i][:size // 2] for i in range(size // 2)]  # matrix[:size][:size]
    b = [matrix[i][size // 2:] for i in range(size // 2)]
    c = [matrix[i][:size // 2] for i in range(size // 2, size)]
    d = [matrix[i][size // 2:] for i in range(size // 2, size)]
    return a, b, c, d


def _shtrasen8_myltyply(matrix1, matrix2, matrix_answ, size):
    if size == 1:
        matrix_answ[0][0] += (matrix1[0][0] * matrix2[0][0])
    else:
        print(matrix_answ)
        a, b, c, d = split_for_matrix(matrix1, size)
        e, f, g, h = split_for_matrix(matrix2, size)
        a_answ, b_answ, c_answ, d_answ = split_for_matrix(matrix_answ, size)
        _shtrasen8_myltyply(a, e, a_answ, size // 2)
        _shtrasen8_myltyply(b, g, a_answ, size // 2)
        _shtrasen8_myltyply(a, f, b_answ, size // 2)
        _shtrasen8_myltyply(b, h, b_answ, size // 2)
        _shtrasen8_myltyply(c, e, c_answ, size // 2)
        _shtrasen8_myltyply(d, g, c_answ, size // 2)
        _shtrasen8_myltyply(c, f, d_answ, size // 2)
        _shtrasen8_myltyply(d, h, d_answ, size // 2)
        print(a_answ,'fdjn')

    ...


def num_in_2(num):
    c = 1
    while c < num:
        c *= 2
    return c


def shtrasen8_myltyply(matrix1, matrix2):
    # save size to change size answ
    normalize_size = num_in_2(max(len(matrix1), len(matrix1[0]), len(matrix2), len(matrix2[0])))
    matrix1 = matrix_size_normalize(matrix1, normalize_size)
    matrix2 = matrix_size_normalize(matrix2, normalize_size)
    matrix_res = matrix_size_normalize([[0]], normalize_size)
    print(normalize_size)
    _shtrasen8_myltyply(matrix1, matrix2, matrix_res, normalize_size)

    return matrix_res
    pass


mat1 = [[1, 2],
        [3, 4]]
mat2 = [[5, 6],
        [7, 8]]

mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
mmat = mat[2:]
mmat[2:] = mmat[2:]
print(mmat,'mmmat')

print(base_matrix_multiply(mat1, mat2))
print(shtrasen8_myltyply(mat1, mat2))
