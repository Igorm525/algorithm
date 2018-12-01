# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
from functools import reduce


def is_multiple(num):
    for divider in range(2, 10):
        if num % divider == 0:
            return 1
    return 0


print("{}".format(reduce(lambda count, n: count + is_multiple(n), range(2, 100))))
