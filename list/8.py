# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

row_counter = 0
matrix = []
while row_counter < 4:
    summary = 0
    col_counter = 0
    row = []
    while col_counter < 4:
        number = int(input(f'Введите {col_counter + 1}е число {row_counter+1}й строки: '))
        row.append(number)
        summary += number
        col_counter += 1
    row.append(summary)
    matrix.append(row)
    row_counter += 1
    print(f'{row_counter}я строка {row}')

print('Матрица:')
for row in matrix:
    print('\t'.join([f'{item}' for item in row]))

