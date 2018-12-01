# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from functools import reduce
from random import randint

array = [randint(0, 100) for _ in range(randint(5, 20))]
_min = _max = array[0]
for i in array:
    if i < _min:
        _min = i
    if i > _max:
        _max = i

min_key = array.index(_min)
max_key = array.index(_max)
keys_between = range(min(min_key, max_key) + 1, max(min_key, max_key))
summary = reduce(lambda acc, key: acc + array[key], keys_between, 0)

print(f'Исходный массив {array}')
print(f'Минимальный {_min} и максимальный {_max}')
print(f'Сумму элементов, находящихся между ними {summary}')

# Задание некорректное, так как в массиве возможны ситуации, когда несколько минимальных и максимальных элементов
# и становится не понятно какие именно элементы складывать
