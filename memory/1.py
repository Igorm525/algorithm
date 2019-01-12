# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Вывод четных и нечетных цифр из последовательности.
import math
import random
import sys


def size(func, param, level=0, acc=0):
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                return acc + size(xx, level + 1, acc)
    return acc + sys.getsizeof(x)


def c(n):
    total = 0
    acc = [0, 0]
    for i in n:
        acc = [acc[0] + 1, acc[1]] if int(i) % 2 else [acc[0], acc[1] + 1]
        total += size(acc)
    return acc, total


for _ in range(100):
    x = ''.join([str(random.randint(0, 9)) for _ in range(random.randint(0, 9))])
    print(f"Для числа {x} памяти затрачено: {size(c, x)]} bytes")


