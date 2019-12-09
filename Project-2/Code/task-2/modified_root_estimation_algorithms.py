from f_function import Ffunction
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
        print("Finished after " + str(n) + " approximation iterations. Approximation is: " + str(m))


def modified_newton_raphson_root_estimation(limit_of_iterations=None):
    # number of iterations executed
    iter_count = 0

    # initialize Xn with -2
    x_n = Ffunction.calc_space[0]

    while True:
        x_np1 = x_n - 1 / (Ffunction.calculate_der_1_f(x_n) / Ffunction.calculate_f(x_n)) \
                - (0.5 * Ffunction.calculate_der_2_f(x_n) / Ffunction.calculate_der_1_f(x_n))

        # print(iter_count)
        # print(x_np1 - x_n)
        # print("===========")
        if limit_of_iterations is None:
            # no specific amount of iterations to be executed was given to the method, so
            # we estimate the stop point of our iterations based on the given t_err (desired precision)
            if abs(x_np1 - x_n <= t_err):
                # we reached the desired precision, so we can now stop the iterations
                break
        else:
            # if we have reached the iteration limit given to the method, we stop the iterations
            if iter_count >= limit_of_iterations:
                break

        x_n = x_np1

        iter_count += 1

    print("Finished after " + str(iter_count) + " iterations, with root estimation: " + str(x_n))


def modified_secant_root_estimation():

    # number of iterations executed
    iter_count = 0

    # index indicator that specifies which X (Xn, Xn+1, Xn+2) should be
    # updated with the value of Xn+3 during the current iteration.
    # The initial value of the indicator is 0 (Xn).
    update_x_ind = 0

    # initialize Xn
    x_n = Ffunction.calc_space[0]

    # initialize Xn+1 with (calc_space[0] + calc_space[1]) / 2 ---> Bad initialization that causes division by zero!
    # x_np1 = (Ffunction.calc_space[0] + Ffunction.calc_space[1]) / 2

    # initialize Xn+1 with 0.1
    x_np1 = 0.1

    # initialize Xn+2
    x_np2 = Ffunction.calc_space[1]

    while True:
        q = Ffunction.calculate_f(x_n) / Ffunction.calculate_f(x_np1)
        r = Ffunction.calculate_f(x_np2) / Ffunction.calculate_f(x_np1)
        s = Ffunction.calculate_f(x_np2) / Ffunction.calculate_f(x_n)

        x_np3 = x_np2 - (r * (r - q) * (x_np2 - x_np1) + (1 - r) * s * (x_np2 - x_n)) / ((q - 1) * (r - 1) * (s - 1))

        # print(iter_count)
        # print(x_np3 - x_np2)
        # print("===========")
        if abs(x_np3 - x_np2) <= t_err:
            # we reached the desired precision, so we can now stop the iterations
            break

        # update the Xn element specified by the update_x_ind
        if update_x_ind == 0:
            x_n = x_np3
        elif update_x_ind == 1:
            x_np1 = x_np3
        elif update_x_ind == 2:
            x_np2 = x_np3

        # increment update_x_ind indicator
        update_x_ind += 1

        # if update_x_ind == 3, it should be reset to 0
        # (thus, indicating the Xn element again and resetting the update process)
        if update_x_ind == 3:
            update_x_ind = 0

        # x_np2 = x_np1
        # x_np1 = x_n
        # x_n = x_np3

        iter_count += 1

    print("Finished after " + str(iter_count) + " iterations, with root estimation: " + str(x_np1))


if __name__ == "__main__":
    print("*** Modified Partitioning Root Estimation ***")
    modified_partitioning_root_estimation()
    print("\n\n*** Modified Newton-Raphson Root Estimation ***")
    modified_newton_raphson_root_estimation()
    print("\n\n*** Modified Secant Root Estimation ***")
    modified_secant_root_estimation()
    print("\n\n*** Modified Newton-Raphson Root estimation for ONLY 10 iterations ***")
    modified_newton_raphson_root_estimation(10)

