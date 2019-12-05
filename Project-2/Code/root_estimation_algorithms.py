import f_function
import math

# Tolerable error for our approximation calculation
t_err = 0.000005


def partitioning_root_estimation():
    # Amount of iterations needed to reach
    # the required estimate accuracy
    n = math.floor(
        (math.log(f_function.calc_space[1] - f_function.calc_space[0], math.e) -
         math.log(t_err, math.e)) / math.log(2, math.e))

    # States whether a root solution was found during the approximation iterations
    found_root = False

    m = 0

    for i in range(n):
        m = (f_function.calc_space[0] + f_function.calc_space[1]) / 2
        f_m = f_function.calculate_f(m)

        if f_m == 0:
            found_root = True
            break
        else:
            f_a = f_function.calculate_f(f_function.calc_space[0])
            if f_m * f_a < 0:
                f_function.calc_space[1] = m
            else:
                f_function.calc_space[0] = m

    if found_root:
        print("A root solution was found: ", m)
    else:
        print("Did " + str(n) + "approximation iterations. Approximation is: " + str(m))


def newton_raphson_root_estimation():
    # flag that states whether to continue the newton-raphson iterations or stop
    stop = False

    # number of iterations executed
    iter_count = 0

    x_n = None

    # initialize Xn-1 with -2
    x_nm1 = f_function.calc_space[0]

    while not stop:
        x_n = x_nm1 - (f_function.calculate_f(x_nm1) / f_function.calculate_der_f(x_nm1))

        print(iter_count)
        print(x_n - x_nm1)
        print("===========")
        if x_n - x_nm1 <= t_err:
            # we reached the desired precision, so we can now stop the iterations
            stop = True

        x_nm1 = x_n

        iter_count += 1

    print("Finished after " + str(iter_count) + " iterations, with root estimation: " + str(x_n))


def secant_root_estimation():
    # flag that states whether to continue the secant approximation iterations or stop
    stop = False

    # number of iterations executed
    iter_count = 0

    # initialize Xn-1 with -2
    x_nm1 = f_function.calc_space[0]

    # initialize Xn with 2
    x_n = f_function.calc_space[1]

    # Xn+1
    x_np1 = None

    while not stop:
        x_np1 = x_n - ((f_function.calculate_f(x_n) * (x_n - x_nm1)) /
                       (f_function.calculate_f(x_n) - f_function.calculate_f(x_nm1)))

        print(iter_count)
        print(x_np1 - x_n)
        print("===========")
        if x_np1 - x_n <= t_err:
            # we reached the desired precision, so we can now stop the iterations
            stop = True

        x_n = x_np1

        iter_count += 1

    print("Finished after " + str(iter_count) + " iterations, with root estimation: " + str(x_np1))


if __name__ == "__main__":
    print("*** Partitioning Root Estimation ***")
    partitioning_root_estimation()
    print("\n\n*** Newton-Raphson Root Estimation ***")
    newton_raphson_root_estimation()
    print("\n\n*** Secant Root Estimation ***")
    secant_root_estimation()

