
def generate_a_matrix(n):
    """" Generates a matrix A of size n according to the rules specified in
    the task's description."""

    # Initialize a_matrix with 0's
    a_matrix = []
    for i in range(n):
        a_matrix.append([0] * n)

    # Initialize x_vector. All the x element values
    # are considered to be 0 before the first iteration.
    x_vector = [0 for i in range(n)]

    # Generate b vector according to the rules specified in
    # the task's description
    b_vector = [1 for i in range(n)]
    b_vector[0] = 3
    b_vector[n - 1] = 3

    for i in range(n):
        for j in range(n):
            if i == j:
                # Case A(i,i) = 5
                a_matrix[i][j] = 5
            elif i+1 == j or i == j+1:
                # Case A(i+1,i) = A(i,i+1) = -2
                a_matrix[i][j] = -2

    print(b_vector)
    for line in a_matrix:
        print(line)


generate_a_matrix(10)