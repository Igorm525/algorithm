# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.


def sub_str_count(s):
    subs = {}
    for j in range(len(s)):
        acc = ''
        for i, char in enumerate(s):
            if i + j < len(s):
                acc += s[i + j]
                subs.update({acc: subs[acc] + 1 if acc in subs else 1})
    return len(subs), subs


s = input('Введите строку: ')
print(f'Количество различных подстрок {sub_str_count(s)[0]}')
print(f'Частота {sub_str_count(s)[1]}')
