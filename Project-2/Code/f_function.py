import math


# The space in which function f is defined
calc_space = [-2, 2]


# Calculates the value of function f for x
def calculate_f(x):
    return math.exp(math.pow(math.sin(x), 3)) + math.pow(x, 6) - 2 * math.pow(x, 4) - math.pow(x, 3) - 1


# Calculates the value of the derivative of function f for x
def calculate_der_f(x):
    return (6 * math.pow(x, 3) - 8 * x - 3) * math.pow(x, 2) + 3 * math.exp(math.pow(math.sin(x), 3)) * math.pow(
        math.sin(x), 2) * math.cos(x)

