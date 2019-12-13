def mult_matrix(M, N):
    """Multiply square matrices of same dimension M and N"""
    # Create an empty result matrix filled with 0's
    result_matrix = []
    for i in range(len(M)):
        result_matrix.append([0] * len(N[0]))

    for i in range(len(M)):
        m_row = M[i]
        for j in range(len(N[0])):
            n_column = []
            for line in range(len(N)):
                n_column.append(N[line][j])

            for k in range(len(m_row)):
                result_matrix[i][j] += m_row[k] * n_column[k]

    return result_matrix



def pivot_matrix(M):
    """Returns the pivoting matrix for M, used in Doolittle's method."""
    m = len(M)

    # Create an identity matrix, with floating point values
    id_mat = [[float(i ==j) for i in range(m)] for j in range(m)]

    # Rearrange the identity matrix such that the largest element of
    # each column of M is placed on the diagonal of M
    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(M[i][j]))
        if j != row:
            # Swap the rows
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat

def lu_decomposition(A):
    """Performs an LU Decomposition of A (which must be square)
    into PA = LU. The function returns P, L and U."""
    n = len(A)

    # Create zero matrices for L and U
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    # Create the pivot matrix P and the multipled matrix PA
    P = pivot_matrix(A)

    #BUG IN LINE 39! PA = mult_matrix(P, A)
    PA = mult_matrix(P, A)

    # Perform the LU Decomposition
    for j in range(n):
        # All diagonal entries of L are set to unity
        L[j][j] = 1.0

        # LaTeX: u_{ij} = a_{ij} - \sum_{k=1}^{i-1} u_{kj} l_{ik}
        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = PA[i][j] - s1

        # LaTeX: l_{ij} = \frac{1}{u_{jj}} (a_{ij} - \sum_{k=1}^{j-1} u_{kj} l_{ik} )
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (PA[i][j] - s2) / U[j][j]

    return (P, L, U)


A = [[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]]
P, L, U = lu_decomposition(A)

print("A:")
print(A)

print("P:")
print(P)

print("L:")
print(L)

print("U:")
print(U)