import math


def f_function(x):
    return math.exp(-math.pow(x, 2))


def simpson(integration_range, partitions_amount):

    partition_size = (integration_range[1] - integration_range[0]) / partitions_amount

    # N = amount of partitions = amount of points - 1
    points_amount = partitions_amount + 1

    points = [integration_range[0]]
    for i in range(1, points_amount):
        points.append(points[i - 1] + partition_size)

    f_sum_1 = 0
    for i in range(1, math.floor((partitions_amount / 2) - 1)):
        f_sum_1 += f_function(points[2 * i])

    f_sum_2 = 0
    for i in range(1, math.floor(partitions_amount / 2)):
        f_sum_2 += f_function(points[2 * i - 1])

    return partition_size / 3 * (f_function(points[0]) + f_function(points[-1]) + 2 * f_sum_1 + 4 * f_sum_2)


# Since we want to perform the trapezoidal sums estimation for 11 points,
# we give 10 as the amount of partitions
print(simpson((0, 1), 8))
