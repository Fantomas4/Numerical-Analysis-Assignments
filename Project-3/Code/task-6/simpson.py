import math


def f_function(x):
    return math.sin(x)


def f_function_4_der(x):
    return math.sin(x)


def calculate_error(integration_range, points):

    partitions_amount = len(points) - 1

    der_4_abs_res = [abs(f_function_4_der(integration_range[0])), f_function_4_der(abs(integration_range[1]))]

    return math.pow(integration_range[1] - integration_range[0], 5) / (180 * math.pow(partitions_amount, 4)) * max(
        der_4_abs_res)


def simpson(integration_range, partitions_amount):

    partition_size = (integration_range[1] - integration_range[0]) / partitions_amount

    # N = amount of partitions = amount of points - 1

    points = [integration_range[0]]
    for i in range(1, partitions_amount + 1):
        points.append(points[i - 1] + partition_size)

    f_sum_1 = 0
    for i in range(1, int((partitions_amount / 2))):
        f_sum_1 += f_function(points[2 * i])

    f_sum_2 = 0
    for i in range(1, int((partitions_amount / 2) + 1)):
        f_sum_2 += f_function(points[2 * i - 1])

    return ((partition_size / 3) * (f_function(points[0]) + f_function(points[-1]) + 2 * f_sum_1 + 4 * f_sum_2),
            calculate_error(integration_range, points))


# Since we want to perform the trapezoidal sums estimation for 11 points,
# we give 10 as the amount of partitions
# Warning! The amount of partitions MUST BE an even number!
target_range = (0, math.pi / 2)
partitions_number = 10

result = simpson(target_range, partitions_number)

print("Trapezoidal Sums estimation: " + str(result[0]))
print("|Error| <= " + str(result[1]))
