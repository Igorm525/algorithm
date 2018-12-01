# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равными (оба являться минимальными), так и различаться.
from random import randint

array = [randint(0, 10) for _ in range(randint(5, 20))]
_min = [min(array[0], array[1]), max(array[0], array[1])]
for i in range(2, len(array)):
    if array[i] < _min[0]:
        _min = [array[i], _min[0]]
    elif array[i] < _min[1]:
        _min[1] = array[i]


print(f'Исходный массив {array}')
print(f'Два наименьших элемента {_min}')

