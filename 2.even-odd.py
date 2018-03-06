def even_odd(n):
    """
    Имея два счетчика для четных и нечетных перебираем цифры числа и проверяем четность
    """
    even = 0
    odd = 0
    left = n
    while True:
        left, digit = divmod(left, 10)
        if digit % 2:
            odd += 1
        else:
            even += 1
        if left == 0:
            break
    return even, odd


if __name__ == '__main__':
    n = int(input('input number: '))
    print(even_odd(n))
