import math


def lagrange_interpolation(input_points, target_x):
    """" Receives a list that contains n+1 input points. Performs
    the Lagrange interpolation based on these points, and calculates the
    approximation of the target point """
    n_p_1 = len(input_points)

    res_sum = 0

    for i in range(n_p_1):
        y_i = input_points[i][1]

        prod_1 = 1
        prod_2 = 1

        for k in range(n_p_1):
            if input_points[i][0] != input_points[k][0]:
                prod_1 *= target_x - input_points[k][0]

                prod_2 *= input_points[i][0] - input_points[k][0]

        l_i = prod_1 / prod_2

        res_sum += y_i * l_i

    return res_sum


# Sampling points (n+1 = 10)
# using 5 decimal digits of accuracy
#
# -π, 0
# -1.8, -0.97384
# -π/2, -1
# -1.2, -0.93203
# 0, 0
# 1, 0.84147
# 1.2, 0.93203
# π/2, 1
# 1.8, 0.97384
# π, 0
# sample_points = [(-3.14159, 0), (-1.8, -0.97384), (-1.57079, -1), (-1.2, -0.93203), (0, 0), (1, 0.84147),
#                  (1.2, 0.93203), (1.57079, 1), (1.8, 0.97384), (3.14159, 0)]


# -3, -0.14112
# -2.5, -0.59847
# -π/2, -1
# -1, -0.84147
# -0.1, -0.09983
# 0.1, 0.09983
# 1, 0.84147
# π/2, 1
# 2.5, 0.59847
# 3, 0.14112
sample_points = [(-3, -0.14112), (-2.5, -0.59847), (-1.57079, -1), (-1, -0.84147), (-0.1, -0.09983), (0.1, 0.09983),
                 (1, 0.84147), (1.57079, 1), (2.5, 0.59847), (3, 0.14112)]

user_input = int(input("Enter x for which the sin(x) Lagrange interpolation will be performed: "))

print("The result is: " + str(lagrange_interpolation(sample_points, user_input)))

