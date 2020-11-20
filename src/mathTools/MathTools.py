import random

basicPrimeNums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
for i in range(0, 40):
    basicPrimeNums.append(i ** 2 + i + 41)


def low_prime_gen():  # This method returns prime numbers form n = {0, 39}
    n = random.randint(0, 39)
    res = n ** 2 + n + 41
    return res


def get_roots(a):
    res = []
    for i in basicPrimeNums:
        if a % i != 0:
            continue
        res.append(i)
        a = a / i
    return res


def euler_phi_function(n):  # This method returns the Euler's phi function to
    aux = n  # a given int n
    res = 1
    roots = get_roots(aux)

    for i in roots:
        res = (1 - 1 / i) * res

    res = res * n
    return int(res)


def null_matrix_crafter(r, c):
    A = [[0 for i in range(r)] for j in range(c)]
    return A


def unit_matrix_crafter(r, c):
    A = null_matrix_crafter(r, c)
    for i in range(r):
        A[i][i] = 1
    return A


def multi_matrix(A, B):
    A_rows = len(A)
    A_columns = len(A[0])
    B_rows = len(B)
    B_columns = len(B[0])

    res = null_matrix_crafter(A_rows, B_columns)

    for i in range(A_rows):
        for j in range(A_columns):
            for k in range(B_columns):
                res[i][j] += A[i][k] * B[k][j]
    return res


def is_coprime(a, b):
    res = True

    for i in get_roots(a):
        for j in get_roots(b):
            if i == j:
                res = False
                break

    return res


def inv_mod(mod, a):
    x = mod
    y = a
    base_matrix = null_matrix_crafter(2, 2)
    base_matrix[0][1] = 1
    base_matrix[1][0] = 1
    product_m = unit_matrix_crafter(2, 2)

    A = [[1],
         [0]]

    B = [[a],
         [mod]]

    quotients = []

    end = False
    'x = y*k + l -> y = l*k` + l`'
    while not end:
        r = int(x / y)
        quotients.append(int(r))
        if x % y == 0:
            end = True
        aux = y
        y = x % y
        x = aux
        if end:
            for i in quotients:
                base_matrix[1][1] = -i
                product_m = multi_matrix(base_matrix, product_m)
    res = product_m[0][1]
    res = res % mod
    return res
