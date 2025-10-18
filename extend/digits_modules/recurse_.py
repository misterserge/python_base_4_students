
import math


def calc_factorial(number):
    if type(number) != int:
        raise ValueError("Number must be an integer")
    if number < 0:
        raise ValueError("Number must be positive")
    # return math.factorial(number)
    if number == 1:
        return 1
    return number * calc_factorial(number - 1)


print('5! =', calc_factorial(5))
print('math.factorial(number)', math.factorial(5))