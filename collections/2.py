# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение — [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque


def addition(x, y):
    memory = 0
    result = deque()
    a = x.pop()
    b = y.pop()
    while a is not False or b is not False:
        summary = int(a) + int(b) + memory
        memory = int(summary > 15)
        summary %= 16
        result.appendleft(summary)
        a = x.pop() if len(x) else False
        b = y.pop() if len(y) else False
    if memory:
        result.appendleft(memory)
    return result


def multiplication(x, y):
    acc_sum = deque()
    b = y.pop()
    shift = 0
    while b is not False:
        memory = 0
        a_deque = deque(x)
        a = a_deque.pop()
        acc_mul = deque()
        while a is not False:
            summary = a * b + memory
            memory = summary // 16
            summary %= 16
            acc_mul.appendleft(summary)
            a = a_deque.pop() if len(a_deque) else False
        if memory:
            acc_mul.appendleft(memory)
        for _ in range(shift):
            acc_mul.append('0')
        acc_sum = addition(acc_sum, acc_mul) if acc_sum else acc_mul
        b = y.pop() if len(y) else False
        shift += 1
    return acc_sum


def hex_ord(x):
    return int(x) if x.isdigit() else ord(x.lower()) - ord('a') + 10


def hex_chr(x):
    return str(x) if x < 10 else chr(x + ord('a') - 10)


def calc(operation, a, b):
    a_decimal_list = list(map(hex_ord, a))
    b_decimal_list = list(map(hex_ord, b))
    result_decimal = operations[operation](a_decimal_list, b_decimal_list)
    return ''.join(map(hex_chr, result_decimal)).upper()


operations = {'+': addition, '*': multiplication}

while True:
    op = input("Введите операцию (+, * или 0 для выхода): ")
    if op == '0':
        break
    first = input("Введите первое число: ")
    second = input("Введите второе число: ")
    print(f"Ответ: {calc(op, first, second)}")

assert calc('+', 'A12', 'F43') == '1955'
assert calc('+', 'fe01', 'ef100') == 'FEF01'
assert calc('+', 'f3f3f4f', 'aef3443') == '1A2E7392'
assert calc('+', 'fff', 'fff') == '1FFE'
assert calc('*', 'A12', 'F43') == '99B0B6'
assert calc('*', 'A2', 'C4F') == '7C9FE'
assert calc('*', 'ef', 'fff') == 'EEF11'
assert calc('*', 'fffffffff', 'fffff') == 'FFFFEFFFF00001'
assert calc('*', 'f0000000f', 'f000f') == 'E100E100E100E1'
