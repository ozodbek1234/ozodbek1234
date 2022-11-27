import math


def sum_numbers_from_one_to_num(num):
    if num:
        return num + sum_numbers_from_one_to_num(num - 1)
    else:
        return 0


result = int(input("Enter a number:"))
x = sum_numbers_from_one_to_num(result)
print(x)

# import math
# print(math.pi)
from math import pi
print(math.sin(pi/2))
print(dir(math))