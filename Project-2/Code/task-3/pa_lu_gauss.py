def multiply_matrices(m1_matrix, m2_matrix):
    """Multiplies the matrices m1_matrix and m2_matrix and returns the result matrix"""
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


def perform_pivoting(m_matrix):
    """Performs any necessary pivoting on m_matrix (making any changes in place)
    and returns its pivoting matrix"""

    m_size = len(m_matrix)

    # Create an identity matrix, with floating point values
    id_matrix = [[float(i == j) for i in range(m_size)] for j in range(m_size)]

    # Rearrange the id_matrix so that the largest absolute element of each column
    # of m_matrix is placed on the diagonal of m_matrix
    for j in range(m_size):
        max_row = j
        max_value = abs(m_matrix[j][j])
        for i in range(j, m_size):
            if abs(m_matrix[i][j]) > max_value:
                max_row = i
                max_value = m_matrix[i][j]

        if j != max_row:
            # Swap the affected rows
            id_matrix[j], id_matrix[max_row] = id_matrix[max_row], id_matrix[j]
            m_matrix[j], m_matrix[max_row] = m_matrix[max_row], m_matrix[j]

    return id_matrix


def perform_pa_lu_decomposition(a_matrix):
    """Performs a PA = LU decomposition on a_matrix (a_matrix must be a square matrix)
     The function returns matrices P, L and U."""

    a_size = len(a_matrix)

    # Create zero matrices for L and U
    l_matrix = []
    for i in range(a_size):
        l_matrix.append([0.0] * a_size)

    u_matrix = []
    for i in range(a_size):
        u_matrix.append([0.0] * a_size)

    # Create the PA matrix, which is the result of A matrix after performing any necessary pivoting
    # Initialize PA matrix using the the A matrix
    pa_matrix = a_matrix.copy()

    # Create the pivot matrix P
    p_matrix = perform_pivoting(pa_matrix)

    # Perform the PA = LU decomposition
    for j in range(a_size):
        # Set all diagonal elements of l_matrix to 1.0
        l_matrix[j][j] = 1.0

        for i in range(j+1):
            s1 = 0
            for k in range(i):
                s1 += u_matrix[k][j] * l_matrix[i][k]

            u_matrix[i][j] = pa_matrix[i][j] - s1

        for i in range(j, a_size):
            s2 = 0
            for k in range(j):
                s2 += u_matrix[k][j] * l_matrix[i][k]

            l_matrix[i][j] = (pa_matrix[i][j] - s2) / u_matrix[j][j]

    return p_matrix, l_matrix, u_matrix


def gauss(a_matrix, b_vector):
    # Perform the PA=LU decomposition of the given A matrix
    p_matrix, l_matrix, u_matrix = perform_pa_lu_decomposition(a_matrix)

    # Ax = b => PAx = Pb => LUx = Pb => Lc = Pb when Ux = c

    # Create c vector
    c_vector = [0.0] * len(l_matrix)

    # Convert b_vector to the format used for matrices
    b_matrix = []
    for elem in b_vector:
        b_matrix.append([float(elem)])

    # Calculate Pb
    pb_matrix = multiply_matrices(p_matrix, b_matrix)

    # Calculate c_vector by solving Lc = Pb
    for c in range(len(c_vector)):
        c_vector[c] = pb_matrix[c][0] - sum(c_vector[j] * l_matrix[c][j] for j in range(c) if c > 0)

    # Create x vector
    x_vector = [0.0] * len(u_matrix)

    # Convert c_vector to the format used for matrices
    c_matrix = []
    for elem in c_vector:
        c_matrix.append([float(elem)])

    # Calculate x_vector by solving Ux = c
    for x in range(len(x_vector) - 1, -1, -1):
        x_vector[x] = c_vector[x] / u_matrix[x][x] - sum(u_matrix[x][j] * x_vector[j] / u_matrix[x][x] for j in range(len(u_matrix) - 1, x, -1))

    return x_vector


A = [[2.0, 1.0, 5.0], [4.0, 4.0, -4.0], [1.0, 3.0, 1.0]]
b = [5.0, 0.0, 6.0]

print("*** Result ***")
print("x vector is: ", gauss(A, b))
