from .f_function import Ffunction
import math
import random

# Tolerable error for our approximation calculation
t_err = 0.000005


def modified_partitioning_root_estimation():
    # Amount of iterations needed to reach
    # the required estimate accuracy
    n = math.floor(
        (math.log(Ffunction.calc_space[1] - Ffunction.calc_space[0], math.e) -
         math.log(t_err, math.e)) / math.log(2, math.e))

    # States whether a root solution was found during the approximation iterations
    found_root = False

    m = 0

    for i in range(n):
        m = random.uniform(Ffunction.calc_space[0], Ffunction.calc_space[1])
        f_m = Ffunction.calculate_f(m)

        if f_m == 0:
            found_root = True
            break
        else:
            f_a = Ffunction.calculate_f(Ffunction.calc_space[0])
            if f_m * f_a < 0:
                Ffunction.calc_space[1] = m
            else:
                Ffunction.calc_space[0] = m

    if found_root:
        print("A root solution was found: ", m)
    else:
        print("Did " + str(n) + "approximation iterations. Approximation is: " + str(m))


def modified_newton_raphson_root_estimation():
    # flag that states whether to continue the newton-raphson iterations or stop
    stop = False

    # number of iterations executed
    iter_count = 0

    x_np1 = None

    # initialize Xn with -2
    x_n = Ffunction.calc_space[0]

    while not stop:
        x_np1 = x_n - 1 / (Ffunction.calculate_der_1_f(x_n) / Ffunction.calculate_f(x_n)) \
                - (0.5 * Ffunction.calculate_der_2_f(x_n) / Ffunction.calculate_der_1_f(x_n))

        print(iter_count)
        print(x_np1 - x_n)
        print("===========")
        if x_np1 - x_n <= t_err:
            # we reached the desired precision, so we can now stop the iterations
            stop = True

        x_n = x_np1

        iter_count += 1

    print("Finished after " + str(iter_count) + " iterations, with root estimation: " + str(x_n))


def modified_secant_root_estimation():
    # flag that states whether to continue the secant approximation iterations or stop
    stop = False

    # number of iterations executed
    iter_count = 0

    # initialize Xn
    x_n = Ffunction.calc_space[0]

    # initialize Xn+1 with (calc_space[0] + calc_space[1]) / 2
    x_np1 = (Ffunction.calc_space[0] + Ffunction.calc_space[1]) / 2

    # initialize Xn+2
    x_np2 = Ffunction.calc_space[1]

    # Xn+3
    x_np3 = None

    while not stop:
        q = Ffunction.calculate_f(x_n) / Ffunction.calculate_f(x_np1)
        r = Ffunction.calculate_f(x_np2) / Ffunction.calculate_f(x_np1)
        s = Ffunction.calculate_f(x_np2) / Ffunction.calculate_f(x_n)

        x_np3 = x_np2 - (r * (r - q) * (x_np2 - x_np1) + (1 - r) * s * (x_np2 - x_n)) / ((q - 1) * (r - 1) * (s - 1))

        print(iter_count)
        print(x_np3 - x_np2)
        print("===========")
        if x_np3 - x_np2 <= t_err:
            # we reached the desired precision, so we can now stop the iterations
            stop = True

        x_np2 = x_np1
        x_np1 = x_n
        x_n = x_np3

        iter_count += 1

    print("Finished after " + str(iter_count) + " iterations, with root estimation: " + str(x_np1))


if __name__ == "__main__":
    print("*** Modified Partitioning Root Estimation ***")
    modified_partitioning_root_estimation()
    print("\n\n*** Modified Newton-Raphson Root Estimation ***")
    modified_newton_raphson_root_estimation()
    print("\n\n*** Modified Secant Root Estimation ***")
    modified_secant_root_estimation()

