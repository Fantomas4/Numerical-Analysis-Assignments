import math


def f_function(x):
    return math.sin(x)


def trapezoidal_sums(integration_range, partitions_amount):

    partition_size = (integration_range[1] - integration_range[0]) / partitions_amount

    # N = amount of partitions = amount of points - 1
    points_amount = partitions_amount + 1

    points = [integration_range[0]]
    for i in range(1, points_amount):
        points.append(points[i - 1] + partition_size)

    f_sum = 0
    for k in range(1, points_amount - 1):
        f_sum += f_function(points[k])

    return partition_size / 2 * (f_function(points[0]) + f_function(points[-1]) + 2 * f_sum)


# Since we want to perform the trapezoidal sums estimation for 11 points,
# we give 10 as the amount of partitions
print(trapezoidal_sums((0, math.pi/2), 10))
