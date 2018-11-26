# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125.. Количество элементов (n) вводится с клавиатуры.

steps = int(input('Введите число: '))

number = total = 1
while steps - 1:
    number /= 2
    total += number
    steps -= 1

print(total)
