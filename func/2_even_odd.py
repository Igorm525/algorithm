# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
from functools import reduce


def even_odd_collector(arrays, x):
    """
    :param arrays: Массив вида [0: [нечетные числа], 1: [четные числа]]
    :param x: Число
    :return: Массив вида [0: [нечетные числа], 1: [четные числа]]
    """
    x = int(x)
    arrays[x % 2].append(x)
    return arrays


n = input('Введите число: ')
(odd, even) = reduce(even_odd_collector, n, [[], []])
print('{} нечетных цифр {} и {} четных цифр {}'.format(len(even), even, len(odd), odd))
