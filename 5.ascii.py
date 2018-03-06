def ascii():
    """
    Перебирая числа от 32 до 127 выводить пары - шаг, значение ascii. Выводим по 10 элементов и перенос
    """
    row = ''
    table = ''
    for char in range(32, 128):
        row += '{}:{}\t'.format(char, chr(char))
        if not (char - 31) % 10:
            table += '{}\n'.format(row)
            row = ''
    table += '{}\n'.format(row)
    return table


if __name__ == '__main__':
    print(ascii())
