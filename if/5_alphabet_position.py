# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

position = int(input("Введите номер буквы: "))
if position < 1 or position > 26:
    raise TypeError('Номер должен находиться в диапазоне от 1 до 26')
char = chr(position + ord('a') - 1)
print(char)

