"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
Перебираем массив. Если число меньше минимума, то запоминаем в min номер шага. Так же с максимумом.
Меняем местами по индексу
"""
numbers = [3,-5,6,2,46,86,65,34,6,5,4,3,-600,45]
min = max = 0
for i, number in enumerate(numbers):
    if numbers[min] > number:
        min = i
    if numbers[max] < number:
        max = i
numbers[min], numbers[max] = numbers[max], numbers[min]
print(numbers)
