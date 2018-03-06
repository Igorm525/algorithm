def sequence(n):
    """
    Во временную переменную записываем 1. Итеративно делим ее пополам n раз. Второй переменной меняем знак
    """
    sign = True
    sum = 0
    figure = 1
    while True:
        if sign:
            sum += figure
        else:
            sum -= figure
        figure /= 2
        sign = not sign
        n -= 1
        if n == 0:
            break
    return sum


if __name__ == '__main__':
    n = int(input('input number: '))
    print(sequence(n))
