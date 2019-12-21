from math import sqrt


def perform_cholesky_decomposition(a_matrix):
    """Performs the Cholesky decomposition on matrix A. Matrix A
    must be a symmetric and positive definite matrix.
    The function returns the lower triangular matrix L."""
    a_size = len(a_matrix)

    # Initialize the L matrix and fill it with 0's
    l_matrix = []
    for i in range(a_size):
        l_matrix.append([0.0] * a_size)

    # Calculate the Cholesky decomposition
    for i in range(a_size):
        for b in range(i + 1):
            temp = sum(l_matrix[i][j] * l_matrix[b][j] for j in range(b))

            if i == b:  # Diagonal elements
                l_matrix[i][b] = sqrt(a_matrix[i][i] - temp)
            else:
                l_matrix[i][b] = (1.0 / l_matrix[b][b] * (a_matrix[i][b] - temp))

    return l_matrix


A = [[6, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]]
L = perform_cholesky_decomposition(A)

print("A:")
for line in A:
    print(line)

print("L:")
for line in L:
    print(line)