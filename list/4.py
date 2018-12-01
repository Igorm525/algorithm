# 4. Определить, какое число в массиве встречается чаще всего.
import operator
from random import randint

array = [randint(0, 6) for _ in range(randint(5, 20))]
counters = {}

for i in array:
    counters[i] = (counters[i] if i in counters else 0) + 1

print(f'Исходный массив {array}')
print(f'Чаще всего встречается {max(counters.items(), key=operator.itemgetter(1))[0]}')

