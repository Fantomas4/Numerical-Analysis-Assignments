import math


# Calculates the value of function f for x
def calculate_f(x):
    return math.exp(math.pow(math.sin(x), 3)) + math.pow(x, 6) - 2 * math.pow(x, 4) - math.pow(x, 3) - 1


if __name__ == "__main__":
    # The space in which function f is defined
    calc_space = [-2, 2]

    # Tolerable error for our approximation calculation
    t_err = 0.000005

    # Amount of iterations needed to reach
    # the required estimate accuracy
    n = math.floor((math.log(calc_space[1] - calc_space[0], math.e) - math.log(t_err, math.e)) / math.log(2, math.e))

    # States whether a root solution was found during the approximation iterations
    found_root = False

    m = 0

    for i in range(n):
        m = (calc_space[0] + calc_space[1]) / 2
        f_m = calculate_f(m)

        if f_m == 0:
            found_root = True
            break
        else:
            f_a = calculate_f(calc_space[0])
            if f_m * f_a < 0:
                calc_space[1] = m
            else:
                calc_space[0] = m

    if found_root:
        print("A root solution was found: ", m)
    else:
        print("Did " + str(n) + "approximation iterations. Approximation is: " + str(m))

# In our exercise, the partitioning algorithm terminates having found the root solution 0
# for the given f function
