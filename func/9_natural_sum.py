# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
from functools import reduce


def summary(string):
    return reduce(lambda acc, x: acc + int(x), string, 0)


def more(a, b):
    return a if summary(a) > summary(b) else b


numbers = input('Введите числа через пробел: ').split()
first = (numbers or [None])[0]
print('Наибольшее по сумме цифр {}'.format(reduce(lambda maximal, x: more(x, maximal), numbers, first)))
