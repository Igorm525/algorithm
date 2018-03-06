import random

if __name__ == '__main__':
    result = random.randint(1, 100)
    step = 0
    while True:
        step += 1
        number = int(input('input number: '))
        if step == 10:
            print('You loose')
            break
        elif number == result:
            print('You win')
            break
        else:
            print('more' if number < result else 'less')

    print(result)
