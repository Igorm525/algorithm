# 1. Отсортируйте по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
import random


def sort(ar):
    left = 1
    right = len(ar) - 1
    while left <= right:
        if ar[left-1] > ar[left]:
            [ar[left], ar[left-1]] = [ar[left-1], ar[left]]
        if left == right:
            left = 0
            right -= 1
        left += 1
    return ar


n = 10
array = [random.randint(-100, 100) for _ in range(n)]
print(f'Исходный массив {array}')
print(f'Отсортированный массив {sort(array)}')
