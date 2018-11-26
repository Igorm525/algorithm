# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

row = ''
table = ''
for char in range(32, 128):
    row += '{}:{}\t'.format(char, chr(char))
    if not (char - 31) % 10:
        table += '{}\n'.format(row)
        row = ''
table += '{}\n'.format(row)
print(table)
