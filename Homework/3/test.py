import numpy as np
def integral(A):
    """

    :param A:
    :return:
    """
    m, n = len(A), len(A[0])
    I = np.zeros((m, n))
    I[0, 0] = A[0, 0]
    for i in range(1, m):
        I[i, 0] = I[i-1, 0] + A[i, 0]
    for j in range(1, n):
        I[0, j] = I[0, j-1] + A[0, j]
    for i in range(1, m):
        for j in range(1, n):
            I[i, j] = I[i-1, j] + I[i, j-1] - I[i-1, j-1] +A[i, j]
    return I


def brute_inte(A):
    I = np.zeros((len(A), len(A[0])))
    for i in range(len(A)):  # O(m)
        for j in range(len(A[0])):   #O(n)
            I[i, j] = np.sum(A[0:i+1, 0:j+1])   # average = O(m/2 * n/2)
    return I  # O(m * n * (m/2) * (n/2))

A = np.random.randint(1, 10, (5, 4))
print(A)
I1 = integral(A)
print(I1)
I2 = brute_inte(A)
print(I2)



