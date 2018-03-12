"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

Перебирая числа из диапазона, проверяем на кратность с введенным числом.
В случае положительного результата инкремент счетчика.

"""


digit = int(input('input digit: '))
number = 2
counter = 0
while True:
    if not number % digit:
        counter += 1
    if number == 99:
        break
    else:
        number += 1
print(counter)
