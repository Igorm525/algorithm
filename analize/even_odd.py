# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
from functools import reduce


# Свертка.
def a(n):
    return reduce(lambda acc, i: [acc[0] + 1, acc[1]] if int(i) % 2 else [acc[0], acc[1] + 1], n, [0, 0])

# python3 -m timeit -n 1000 -s "import even_odd" "even_odd.a('456789878798797987')"
# 1000 loops, best of 5: 6.93 usec per loop

# cProfile.run("a('456789878798797987')")
# 23 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 even_odd.py:6(a)
#        18    0.000    0.000    0.000    0.000 even_odd.py:7(<lambda>)
#         1    0.000    0.000    0.000    0.000 {built-in method _functools.reduce}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Рекурсия.
def b(n):
    def recursion(n, acc):
        acc = [acc[0] + 1, acc[1]] if int(n[0]) % 2 else [acc[0], acc[1] + 1]
        return acc if len(n) == 1 else recursion(n[1:], acc)
    return recursion(n, [0, 0])

# python3 -m timeit -n 1000 -s "import even_odd" "even_odd.b('456789878798797987')"
# 1000 loops, best of 5: 10.4 usec per loop

# cProfile.run("b('456789878798797987')")
# 40 function calls (23 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 even_odd.py:26(b)
#      18/1    0.000    0.000    0.000    0.000 even_odd.py:27(recursion)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        18    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Цикл.
def c(n):
    acc = [0, 0]
    for i in n:
        acc = [acc[0] + 1, acc[1]] if int(i) % 2 else [acc[0], acc[1] + 1]
    return acc

# python3 -m timeit -n 1000 -s "import even_odd" "even_odd.c('456789878798797987')"
# 1000 loops, best of 5: 5.66 usec per loop

# cProfile.run("c('456789878798797987')")
# 4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 even_odd.py:49(c)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
