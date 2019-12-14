from math import sqrt


def calculate_cholesky(A):
    """Calculates the Cholesky decomposition of matrix A. Matrix A
    must be a symmetric and positive definite matrix.
    The function returns the lower triangular matrix L."""
    a_size = len(A)

    # Initialize the L matrix and fill it with 0's
    l_matrix = []
    for i in range(a_size):
        l_matrix.append([0.0] * a_size)

    # Calculate the Cholesky decomposition
    for i in range(a_size):
        for b in range(i + 1):
            temp = sum(l_matrix[i][j] * l_matrix[b][j] for j in range(b))

            if i == b:  # Diagonal elements
                # LaTeX: l_{kk} = \sqrt{ a_{kk} - \sum^{b-1}_{j=1} l^2_{kj}}
                l_matrix[i][b] = sqrt(A[i][i] - temp)
            else:
                # LaTeX: l_{ik} = \frac{1}{l_{kk}} \left( a_{ik} - \sum^{b-1}_{j=1} l_{ij} l_{kj} \right)
                l_matrix[i][b] = (1.0 / l_matrix[b][b] * (A[i][b] - temp))
    return l_matrix


A = [[6, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]]
L = calculate_cholesky(A)

print("A:")
for line in A:
    print(line)

print("L:")
for line in L:
    print(line)