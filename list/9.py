# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint


def tab_list(array):
    return '\t\t'.join([f'{item}' for item in array])


min_num = -10
max_num = 100
min_height = 1
max_height = 10
min_width = 5
max_width = 10

row = range(randint(min_width, max_width))
matrix = [[randint(min_num, max_num) for _ in row] for _ in range(randint(min_height, max_height))]

col_min = {}
row_count = 0
while row_count < len(matrix):
    col_count = 0
    while col_count < len(matrix[row_count]):
        current = matrix[row_count][col_count]
        if col_count not in col_min or current < col_min[col_count]:
            col_min[col_count] = current
        col_count += 1
    row_count += 1

print('Матрица:')
for row in matrix:
    print(tab_list(row))

minimals = tab_list(col_min.values())
print(f'Минимальные элементы по колонкам:\n{minimals}')
print(f'Максимальное значение:\n{max(col_min.values())}')
