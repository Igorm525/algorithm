"""
 Определить, какое число в массиве встречается чаще всего.

 Перебираем массив. Создаем массив с ключем - число, значением -  кол-во вхождений. Выводим ключ наибольшего значения"
"""
numbers = [3,-5,6,2,46,86,6, 3,4,-600,2,2,2,5,34,6,5,4,3,-600,45]
i = 0
dictionary = {}
for i, number in enumerate(numbers):
    if numbers[i] in dictionary:
        dictionary[numbers[i]] += 1
    else:
        dictionary[numbers[i]] = 1
print(max(dictionary, key=dictionary.get))
