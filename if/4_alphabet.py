# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

first = input("Введите первую букву: ")
second = input("Введите вторую букву: ")
(first_position, second_position) = map(lambda char: ord(str.lower(char[0])) - ord('a') + 1, (first, second))

out = 'Буква "{}" находится на {}й позиции, буква "{}" на {}й, между ними {} букв(a)'

print(out.format(first, first_position, second, second_position, abs(second_position - first_position)))
