import math


# Calculates f(x)
def f_function(x):
    return math.sin(x)


# Calculates f"(x)
def f_function_der_2(x):
    return -math.sin(x)


# Calculates the error for the given trapezoidal sums approximation
def calculate_error(integration_range, points):

    partitions_amount = len(points) - 1

    der_2_abs_res = []
    for x in range(len(points)):
        der_2_abs_res.append(abs(f_function_der_2(x)))

    return math.pow(integration_range[1] - integration_range[0], 3) / 12 * math.pow(
        partitions_amount, 2) * max(der_2_abs_res)


# Performs a trapezoidal sums approximation on the given integration range and with
# the given amount of partitions and returns the result
def trapezoidal_sums(integration_range, partitions_amount):

    partition_size = (integration_range[1] - integration_range[0]) / partitions_amount

    # N = amount of partitions = amount of points - 1
    points_amount = partitions_amount + 1

    points = [integration_range[0]]
    for i in range(1, points_amount):
        points.append(points[i - 1] + partition_size)

    f_sum = 0
    for k in range(1, partitions_amount):
        f_sum += f_function(points[k])

    return partition_size / 2 * (f_function(points[0]) + f_function(points[-1]) + 2 * f_sum), calculate_error(
        integration_range, points)


# Since we want to perform the trapezoidal sums estimation for 11 points,
# we give 10 as the amount of partitions
print(trapezoidal_sums((0, math.pi/2), 10))
