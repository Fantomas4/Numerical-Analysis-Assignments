def multiply_matrices(m1_matrix, m2_matrix):
    """Multiplies the square matrices m1_matrix and m2_matrix that are of equal dimensions"""
    # Create an empty result matrix filled with 0's
    result_matrix = []
    for i in range(len(m1_matrix)):
        result_matrix.append([0] * len(m2_matrix[0]))

    for i in range(len(m1_matrix)):
        m_row = m1_matrix[i]
        for j in range(len(m2_matrix[0])):
            n_column = []
            for b in range(len(m2_matrix)):
                n_column.append(m2_matrix[b][j])

            for k in range(len(m_row)):
                result_matrix[i][j] += m_row[k] * n_column[k]

    return result_matrix


def calculate_pivot_matrix(m_matrix):
    """Returns the pivoting matrix for m_matrix, used in Doolittle's PA = LU decomposition method."""
    m_size = len(m_matrix)

    # Create an identity matrix, with floating point values
    id_matrix = [[float(i == j) for i in range(m_size)] for j in range(m_size)]

    # Rearrange the id_matrix so that the largest element of each column
    # of m_matrix is placed on the diagonal of m_matrix
    for j in range(m_size):
        row = max(range(j, m_size), key=lambda i: abs(m_matrix[i][j]))
        if j != row:
            # Swap the rows
            id_matrix[j], id_matrix[row] = id_matrix[row], id_matrix[j]

    return id_matrix


def perform_pa_lu_decomposition(a_matrix):
    """Performs a PA = LU decomposition on a_matrix (a_matrix must be a square matrix)
     The function returns matrices P, L and U."""

    n = len(a_matrix)

    # Create zero matrices for L and U
    l_matrix = []
    for i in range(n):
        l_matrix.append([0.0] * n)

    u_matrix = []
    for i in range(n):
        u_matrix.append([0.0] * n)

    # Create the pivot matrix P
    p_matrix = calculate_pivot_matrix(a_matrix)

    # Create the PA matrix, which is the product of matrices P and A
    pa_matrix = multiply_matrices(p_matrix, a_matrix)

    # Perform the PA = LU decomposition
    for j in range(n):
        # Set all diagonal elements of l_matrix to 1.0
        l_matrix[j][j] = 1.0

        # LaTeX: u_{ij} = a_{ij} - \sum_{k=1}^{i-1} u_{kj} l_{ik}
        for i in range(j+1):
            s1 = sum(u_matrix[k][j] * l_matrix[i][k] for k in range(i))
            u_matrix[i][j] = pa_matrix[i][j] - s1

        # LaTeX: l_{ij} = \frac{1}{u_{jj}} (a_{ij} - \sum_{k=1}^{j-1} u_{kj} l_{ik} )
        for i in range(j, n):
            s2 = sum(u_matrix[k][j] * l_matrix[i][k] for k in range(j))
            l_matrix[i][j] = (pa_matrix[i][j] - s2) / u_matrix[j][j]

    return p_matrix, l_matrix, u_matrix


A = [[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]]
P, L, U = perform_pa_lu_decomposition(A)

print("\nA:")
for line in A:
    print(line)

print("\nP:")
for line in P:
    print(line)

print("\nL:")
for line in L:
    print(line)

print("\nU:")
for line in U:
    print(line)
