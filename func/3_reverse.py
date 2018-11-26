# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
from functools import reduce

number = input('Введите число: ')
print(''.join(reduce(lambda reverse, char: [char] + reverse, number, [])))
