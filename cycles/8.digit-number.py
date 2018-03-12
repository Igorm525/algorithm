def part(number, digit):
    """
     Функция разбивает введенное число на левую часть и правую цифру
     Возвращает результат сравнения правой цифры с введенной, складывая рекурсивно с левой частью
    """
    left, right = divmod(number, 10)
    quantity = int(right == digit)
    return quantity + part(left, digit) if left > 0 else quantity


if __name__ == '__main__':
    d = int(input('input digit: '))
    n = int(input('input number: '))
    print(part(n, d))


