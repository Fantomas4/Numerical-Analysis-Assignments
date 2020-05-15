import math


class Ffunction:

    # The space in which function f is defined
    calc_space = [-2, 2]

    # Calculates the value of function f for x
    @staticmethod
    def calculate_f(x):
        return math.exp(math.pow(math.sin(x), 3)) + math.pow(x, 6) - 2 * math.pow(x, 4) - math.pow(x, 3) - 1

    # Calculates the value of the first derivative of function f for x
    @staticmethod
    def calculate_der_1_f(x):
        return (6 * math.pow(x, 3) - 8 * x - 3) * math.pow(x, 2) + 3 * math.exp(math.pow(math.sin(x), 3)) * math.pow(
            math.sin(x), 2) * math.cos(x)

    # Calculates the value of the second derivative of function f for x
    @staticmethod
    def calculate_der_2_f(x):
        return 30 * math.pow(x, 4) - 24 * math.pow(x, 2) - 6 * x - 3 * math.exp(math.pow(math.sin(x), 3)) \
               * math.pow(math.sin(x), 3) + 6 * math.exp(math.pow(math.sin(x), 3)) * math.sin(x) * math.pow(math.cos(x), 2) \
               + 9 * math.exp(math.pow(math.sin(x), 3)) * math.pow(math.sin(x), 4) * math.pow(math.cos(x), 2)
