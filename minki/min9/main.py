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


def num_in_2(num):
    c = 1
    while c < num:
        c *= 2
    return c


def split_for_matrix(matrix, size):
    a = [matrix[i][:size // 2] for i in range(size // 2)]  # matrix[:size][:size]
    b = [matrix[i][size // 2:] for i in range(size // 2)]
    c = [matrix[i][:size // 2] for i in range(size // 2, size)]
    d = [matrix[i][size // 2:] for i in range(size // 2, size)]
    return a, b, c, d


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def _shtrasen8_myltyply(matrix1, matrix2, matrix_answ, size):
    if size == 1:
        matrix_answ[0][0] += (matrix1[0][0] * matrix2[0][0])
    else:
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
        # всё что ниже можно убрать, если split_for_matrix будет отдавать ссылки на элементы массива, переделаю
        for i in range(size // 2):
            for j in range(size // 2):
                matrix_answ[i][j] = a_answ[i][j]
                matrix_answ[i][j + size // 2] = b_answ[i][j]
                matrix_answ[i + size // 2][j] = c_answ[i][j]
                matrix_answ[i + size // 2][j + size // 2] = d_answ[i][j]


def shtrasen8_myltyply(matrix1, matrix2):
    # save size to change size answ
    matrix_answ_x = len(matrix1)
    matrix_answ_y = len(matrix2[0])
    normalize_size = num_in_2(max(len(matrix1), len(matrix1[0]), len(matrix2), len(matrix2[0])))
    matrix1 = matrix_size_normalize(matrix1, normalize_size)
    matrix2 = matrix_size_normalize(matrix2, normalize_size)
    matrix_res = matrix_size_normalize([[0]], normalize_size)
    _shtrasen8_myltyply(matrix1, matrix2, matrix_res, normalize_size)

    matrix_res = [matrix_res[i][:matrix_answ_y] for i in range(matrix_answ_x)]

    return matrix_res


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def matr_summ(matr1, matr2):
    for i in range(len(matr1)):
        for j in range(len(matr1[0])):
            matr1[i][j] += matr2[i][j]
    return matr1


def matr_subtraction(matr1, matr2):
    for i in range(len(matr1)):
        for j in range(len(matr1[0])):
            matr1[i][j] -= matr2[i][j]
    return matr1


def _shtrasen7_myltyply(matrix1, matrix2, size):
    if size == 1:
        return [[matrix1[0][0] * matrix2[0][0]]]
    else:
        a, b, c, d = split_for_matrix(matrix1, size)
        e, f, g, h = split_for_matrix(matrix2, size)

        p1 = _shtrasen7_myltyply(a, matr_subtraction(f, h),size//2)
        p2 = _shtrasen7_myltyply(matr_summ(a, b), h,size//2)
        p3 = _shtrasen7_myltyply(matr_summ(c, d), e,size//2)
        p4 = _shtrasen7_myltyply(d, matr_subtraction(g, e),size//2)
        p5 = _shtrasen7_myltyply(matr_summ(a, d), matr_summ(e, h),size//2)
        p6 = _shtrasen7_myltyply(matr_subtraction(b, d), matr_summ(g, h),size//2)
        p7 = _shtrasen7_myltyply(matr_subtraction(a, c), matr_summ(e, f),size//2)

        a_answ = matr_summ(matr_subtraction(matr_summ(p5, p4), p2), p6)
        b_answ = matr_summ(p1, p2)
        c_answ = matr_summ(p3, p4)
        d_answ = matr_subtraction(matr_subtraction(matr_summ(p1, p5), p3), p7)

        matrix_answ = matrix_size_normalize([[0]], size)
        for i in range(size // 2):
            for j in range(size // 2):
                matrix_answ[i][j] = a_answ[i][j]
                matrix_answ[i][j + size // 2] = b_answ[i][j]
                matrix_answ[i + size // 2][j] = c_answ[i][j]
                matrix_answ[i + size // 2][j + size // 2] = d_answ[i][j]
        return matrix_answ


def shtrasen7_myltyply(matrix1, matrix2):
    # save size to change size answ
    matrix_answ_x = len(matrix1)
    matrix_answ_y = len(matrix2[0])
    normalize_size = num_in_2(max(len(matrix1), len(matrix1[0]), len(matrix2), len(matrix2[0])))
    matrix1 = matrix_size_normalize(matrix1, normalize_size)
    matrix2 = matrix_size_normalize(matrix2, normalize_size)
    matrix_res = _shtrasen7_myltyply(matrix1, matrix2, normalize_size)

    matrix_res = [matrix_res[i][:matrix_answ_y] for i in range(matrix_answ_x)]

    return matrix_res


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


mat1 = [[1, 2],
        [3, 4],
        [9, 10]]
mat2 = [[5, 6, 11],
        [7, 8, 12]]

print(base_matrix_multiply(mat1, mat2))
print(shtrasen8_myltyply(mat1, mat2))
print(shtrasen7_myltyply(mat1, mat2))

print(base_matrix_multiply(mat2, mat1))
print(shtrasen8_myltyply(mat2, mat1))
print(shtrasen7_myltyply(mat2, mat1))
