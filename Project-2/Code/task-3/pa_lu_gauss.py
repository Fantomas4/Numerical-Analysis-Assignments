# The function takes the A matrix (2D, square) as input and produces a unit lower triangular
# matrix L, an upper triangular matrix U and a permutation vector P, so that
# P * A = L * U
def perform_pa_lu_decomposition(a_matrix):

    # A matrix is a list of lists, each representing a row
    print("Input-> A matrix is:")
    for line in a_matrix:
        print(*line)

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

    for col in range(a_size):

        # The current pivot element's position in [row, column] format
        pivot_pos = [col, col]

        for row in range(pivot_pos[0] + 1, a_size):

            # Find the maximum element of the pivot's column,
            # searching from the pivot element's position and below
            max_pos = [pivot_pos[0], pivot_pos[1]]
            max_value = a_matrix[max_pos[0]][max_pos[1]]

            for line in range(pivot_pos[0] + 1, a_size):
                if abs(a_matrix[line][col]) > abs(max_value):
                    max_value = a_matrix[line][col]
                    max_pos = [line, col]

            # If an element below the pivot is found to have a greater value than it,
            # swap the pivot's row with the max element's row
            if max_pos != pivot_pos:
                # Get the pivot's row
                # pivot_row = [a_matrix[pivot_pos[0]][k] for k in range(a_size)]
                pivot_row = a_matrix[pivot_pos[0]]

                # Get the max element's row
                max_row = a_matrix[max_pos[0]]

                # Swap the rows in A matrix
                a_matrix[pivot_pos[0]] = max_row
                a_matrix[max_pos[0]] = pivot_row

                # Modify the permutation vector P
                temp = p_vector[pivot_pos[0]]
                p_vector[pivot_pos[0]] = p_vector[max_pos[0]]
                p_vector[max_pos[0]] = temp

            # Make all elements below the pivot element zero.
            # To do that, we will make matrix calculations between the pivot's row
            # and each of the target rows

            # Get the pivot element's value
            pivot_elem = a_matrix[pivot_pos[0]][pivot_pos[1]]

            for r in range(pivot_pos[0] + 1, a_size):
                # Get the column element's whole row
                target_row = a_matrix[r]

                # For each element of the target row, starting from the element at the same column as the pivot,
                # perform the matrix calculations
                for elem in range(pivot_pos[1], len(target_row)):
                    target_row[elem] = target_row[elem] + pivot_elem * (- target_row[pivot_pos[1]] / pivot_elem)

                # Place the modified row back to A matrix
                a_matrix[r] = target_row

    print("Result-> A matrix is: ")
    for line in a_matrix:
        print(*line)

# test_matrix = []
# test_matrix.append([2, 4, 1])
# test_matrix.append([-1, -2, 2])
# test_matrix.append([4, 2, -3])
test_matrix = []
test_matrix.append([1.383, 0.1, 0.5])
test_matrix.append([0.0077, 0.1, 0.1976])
test_matrix.append([-2.6452, -1.383, 1.9127])

perform_pa_lu_decomposition(test_matrix)












