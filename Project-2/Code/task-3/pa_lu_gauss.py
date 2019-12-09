
# The function takes the A matrix (2D, square) as input and produces a unit lower triangular
# matrix L, an upper triangular matrix U and a permutation vector P, so that
# P * A = L * U
def perform_pa_lu_decomposition(a_matrix):

    # Calculate the size of A matrix
    a_size = len(a_matrix)

    # Create the permutation matrix P
    p_matrix = []

    for col in range(a_size):

        cur_col = []

        for line in range(a_size):
            if col == line:
                cur_col.append(1)
            else:
                cur_col.append(0)

        p_matrix.append(cur_col)

    for col in range(a_size):
        # Find the position of the first matrix element under the
        # diagonal for the current column





