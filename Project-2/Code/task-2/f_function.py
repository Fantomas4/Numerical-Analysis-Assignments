import math


class Ffunction:
    # The space in which function f is defined
    calc_space = [-2, 2]

    # Calculates the value of function f for x
    @staticmethod
    def calculate_f(x):
        return 54 * math.pow(x, 6) + 45 * math.pow(x, 5) - 102 * math.pow(x, 4) - 69 * math.pow(x, 3) + 35 \
               * math.pow(x, 2) + 16 * x - 4

    # Calculates the value of the first derivative of function f for x
    @staticmethod
    def calculate_der_1_f(x):
        return 324 * math.pow(x, 5) + 225 * math.pow(x, 4) - 408 * math.pow(x, 3) - 207 * math.pow(x, 2) + 70 * x + 16

    # Calculates the value of the second derivative of function f for x
    @staticmethod
    def calculate_der_2_f(x):
        return 1620 * math.pow(x, 4) + 900 * math.pow(x, 3) - 1224 * math.pow(x, 2) - 414 * x + 70
