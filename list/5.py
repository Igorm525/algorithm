# 5. Найти в массиве максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
from random import randint

array = [randint(-100, 100) for _ in range(randint(5, 20))]
_max = [None, 0]
for key, value in enumerate(array):
    if value < _max[1] and value < 0:
        _max = [key, value]

print(f'Исходный массив {array}')
if _max[0] is not None:
    print(f'Максимальный отрицательный элемент на позиции {_max[0]} со значением {_max[1]}')
else:
    print(f'Отрицательных элементов не найдено')
