# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

array = [randint(0, 100) for _ in range(randint(5, 20))]
_min = _max = array[0]
for key, value in enumerate(array):
    if value < _min:
        _min = value
        min_key = key
    if value > _max:
        _max = value
        max_key = key

print(f'Исходный массив {array}')
array[min_key], array[max_key] = array[max_key], array[min_key]
print(f'Выходной массив {array}')

