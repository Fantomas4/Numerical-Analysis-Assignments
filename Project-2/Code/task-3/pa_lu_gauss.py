# The function takes the A matrix (2D, square) as input and produces a unit lower triangular
# matrix L, an upper triangular matrix U and a permutation vector P, so that
# P * A = L * U
def perform_pa_lu_decomposition(a_matrix):
    # Calculate the size of A matrix
    a_size = len(a_matrix)

    # # Create the permutation matrix P
    # p_matrix = []
    #
    # for col in range(a_size):
    #
    #     cur_col = []
    #
    #     for line in range(a_size):
    #         if col == line:
    #             cur_col.append(1)
    #         else:
    #             cur_col.append(0)
    #
    #     p_matrix.append(cur_col)

    # Create a vector representing the permutation vector P
    p_vector = [i for i in range(a_size)]

    # The current pivot element's position in [row, column] format
    pivot_pos = [0, 0]

    for col in range(a_size):
        # Find the maximum element of the pivot's column,
        # searching from the diagonal's element in the pivot's column and below
        max_pos = [pivot_pos[1], pivot_pos[1]]
        max_value = a_matrix[max_pos[0], max_pos[1]]

        for line in range(pivot_pos[0] + 1, a_size):
            if a_matrix[line][col] > max_value:
                max_value = a_matrix[line][col]
                max_pos = [line, col]

        # If an element below the pivot is found to have a greater value than it,
        # swap the pivot's row with the max element's row
        if max_pos != pivot_pos:
            # Get the pivot's row
            pivot_row = [a_matrix[pivot_pos[0]][k] for k in range(a_size)]

            # Get the max element's row
            max_row = [a_matrix[max_pos[0]][k] for k in range(a_size)]

            # Swap the rows in A matrix
            a_matrix[pivot_pos[0]] = max_row
            a_matrix[max_pos[0]] = pivot_row

            # Update pivot_pos value
            pivot_pos = max_pos

        # Make all elements below the main diagonal element zero.
        # To do that, we will make matrix calculations between the pivot's row
        # and each of the target rows

        # First, find the diagonal element of our column
        diag_elem_pos = [pivot_pos[0], pivot_pos[0]]

        # Get the whole row where the pivot is located
        pivot_row = a_matrix[pivot_pos[0]]

        for row in range(pivot_pos[0] + 1, a_size):
            # Get the column element's whole row
            target_row = a_matrix[row]

            # For each element of the target row, perform the matrix calculations













