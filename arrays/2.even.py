"""
Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

Перебираем первый массив, и если попадается четное число то добавляем значение шага во второй массив

"""
numbers = [3,5,6,2,46,86,65,34,6,5,4,3,6,45]
evens = []
for i, number in enumerate(numbers):
    if not number % 2:
        evens.append(i)
print(evens)
