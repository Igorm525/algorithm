def inverted(number):
    """
    Перебираем цифры числа, делим каждое на rank, которое в свою очередь итеративно увеличивается в 10 раз. Возвращаем сумму полученных значений умноженных на rank
    """
    inverted = 0
    rank = 1
    left = number
    while True:
        left, digit = divmod(left, 10)
        inverted += digit / rank
        if left == 0:
            break
        else:
            rank *= 10
    return int(inverted * rank)


if __name__ == '__main__':
    n = int(input('input number: '))
    print(inverted(n))
