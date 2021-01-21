import random

basicPrimeNums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
for i in range(0, 40):
    basicPrimeNums.append(i ** 2 + i + 41)


def low_prime_gen():  # This method returns prime numbers form n = {0, 39}
    n = random.randint(37, len(basicPrimeNums) - 1)
    res = basicPrimeNums[n]
    return res


def get_roots(a):  # Return the divisors of int a
    res = []
    for i in basicPrimeNums:
        if a % i != 0:
            continue
        res.append(i)
        a = a / i
    return res


def euler_phi_function(p, q):  # This method returns the Euler's phi function to a given int n

    res = (p - 1) * (q - 1)

    return res


def null_matrix_crafter(r, c):  # Returns a Null Matrix fo the wanted size.
    A = [[0 for i in range(r)] for j in range(c)]
    return A


def multi_matrix(A, B):  # Returns the result of A * B, being A and B the given matrix.
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


def euclid_extended(a, b):  # Returns MCD of given a and b ints.
    x = a
    y = b
    r = 1
    while r != 0:
        r = x % y
        x = y
        y = r
    return x


def is_coprime(a, b):  # Returns a boolean value, True if a and b are coprimes, False if they're not.
    res = euclid_extended(a, b)
    if res == 1:
        res = True
    else:
        res = False
    return res


def inv_mod(mod, a):  # Returns the value of modular inverse of a for a given mod
    for i in range(1, mod):
        if (a * i) % mod == 1:
            return i
    return None
