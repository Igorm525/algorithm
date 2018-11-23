# 3. Написать программу, которая генерирует в указанных пользователем границах:
#  - случайное целое число,
#  - случайное вещественное число,
#  - случайный символ.
#  Для каждого из трех случаев пользователь задает свои границы диапазона.
#  Например, если надо получить случайный символ от 'a' до 'f', вводятся эти символы.
#  Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно. 

import random

# Входная и выходная обработка для каждого типа
char_type_io = {
    '': (lambda value: ord(value[0]), lambda value: chr(int(value))),
    'i': (lambda value: int(value), lambda value: int(value)),
    'f': (lambda value: float(value), lambda value: value)
}


def range_random(char_type=None, left=None, right=None):
    char_type = char_type if char_type is not None else input("Введите тип границ: целое(i), вещественное(f) число, по умолчанию символ: ")

    if char_type not in char_type_io:
        raise TypeError('Неверный тип границ')

    left = left or input("Введите левую границy диапазона: ")
    right = right or input("Введите правую границy диапазона: ")

    # Приводим границы к соответствующему типу
    (left_typed, right_typed) = map(lambda value: char_type_io[char_type][0](value), (left, right))

    random_position = (right_typed - left_typed) * random.random() + left_typed

    # Приводим случайное значение к соответствующему типу
    random_char = char_type_io[char_type][1](random_position)

    return 'Получено случайное значение "{}" в диапазоне от "{}" до "{}"'.format(random_char, left, right)


print(range_random())

print(range_random('', 'a', 'z'))
print(range_random('', 'a', 'z'))
print(range_random('', 'a', 'z'))

print(range_random('', 'A', 'Z'))
print(range_random('', 'A', 'Z'))
print(range_random('', 'A', 'Z'))

print(range_random('i', 1, 10))
print(range_random('i', 1, 10))
print(range_random('i', 1, 10))

print(range_random('i', -100, 100))
print(range_random('i', -100, 100))
print(range_random('i', -100, 100))

print(range_random('f', 0.40, 0.70))
print(range_random('f', 0.40, 0.70))
print(range_random('f', 0.40, 0.70))

print(range_random('f', 0.40, 9.70))
print(range_random('f', 0.40, 9.70))
print(range_random('f', 0.40, 9.70))
