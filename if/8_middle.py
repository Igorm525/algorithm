# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

(a, b, c) = input("Введите три числа через запятую(пример 3 5 2): ").split()

# Приводим к int
(a, b, c) = map(lambda x: int(x), (a, b, c))

if b < a < c or c < a < b:
    middle = a
elif a < b < c or c < b < a:
    middle = b
else:
    middle = c


print('Среднее число {}'.format(middle))
