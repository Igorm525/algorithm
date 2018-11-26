# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа должна не завершаться,
# а запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '★', '/'),
# программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


def calc(operation, x, y):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    return False if operation == '/' and y == 0 else operations[operation](x, y)


while True:
    sign = input("Введите операцию('+', '-', '★', '/') или выход('0'): ")
    if sign == '0':
        break
    if sign not in ('+', '-', '*', '/', '0'):
        print('Неверная операция')
        continue
    first = int(input("Введите первый операнд: "))
    while True:
        second = int(input("Введите второй операнд: "))
        if sign == '/' and second == 0:
            print('На ноль делить нельзя')
        else:
            break
    print('Результат операции {} {} {} равен: {}'.format(first, sign, second, calc(sign, first, second)))

assert calc('+', 0, 2) == 2
assert calc('+', 1, 2) == 3
assert calc('+', 1, 0) == 1
assert calc('-', 0, 2) == -2
assert calc('-', 0, 0) == 0
assert calc('-', 1, 0) == 1
assert calc('*', 1, 0) == 0
assert calc('*', -1, 0) == 0
assert calc('*', -1, -1) == 1
assert calc('/', -1, -1) == 1
assert not calc('/', -1, 0)
assert calc('/', 8, 9) < 1

