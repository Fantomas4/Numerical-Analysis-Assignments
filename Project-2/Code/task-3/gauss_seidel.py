# t_err specifies the required precision for our calculations.
# A value of 0.00005 specifies a precision of 4 floating point numbers
# (with rounding).
t_err = 0.00005


def calculate_vector_diff(vector_1, vector_2):
    """ Takes 2 vectors and returns a new vector, which is the result of the subtraction
    vector_1 - vector_2 """

    result_vector = []
    for i, elem in enumerate(vector_1):
        result_vector.append(elem - vector_2[i])

    return result_vector


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

    print("b_vector is: ", b_vector)
    print("a_matrix is: ")
    for line in a_matrix:
        print(line)

    while True:
        old_x_vector = x_vector.copy()
        for i in range(n):
            x_vector[i] = 1/a_matrix[i][i] * (b_vector[i] - sum(a_matrix[i][j] * x_vector[j] for j in range(i - 1)) -
                                              sum(a_matrix[i][j] * old_x_vector[j] for j in range(i + 1, n)))

        # Calculate the infinite norm of x_vector - old_x_vector
        infinity_norm = max(abs(elem) for elem in calculate_vector_diff(x_vector, old_x_vector))

        if infinity_norm <= t_err:
            # The specified precision has been achieved
            # so we can now break the loop.
            break

    return x_vector


result = generate_a_matrix(5)
print("Result returned is: ", result)
