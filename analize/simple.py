def eratosthenes(n):
    _range = list(range(2, n + 1))
    for i in _range:
        if i != 0:
            for candidate in range(2 * i, n+1, i):
                _range[candidate-2] = 0
    return list(filter(lambda x: bool(x), _range))

# python3 -m timeit -n 1000 -s "import simple" "simple.eratosthenes(10)"
# 1000 loops, best of 5: 4.3 usec per loop

# python3 -m timeit -n 1000 -s "import simple" "simple.eratosthenes(100)"
# 1000 loops, best of 5: 33.8 usec per loop

# python3 -m timeit -n 1000 -s "import simple" "simple.eratosthenes(1000)"
# 1000 loops, best of 5: 376 usec per loop

# python3 -m timeit -n 1000 -s "import simple" "simple.eratosthenes(10000)"
# 1000 loops, best of 5: 4.02 msec per loop

# cProfile.run("eratosthenes(10000)")
# 10003 function calls in 0.010 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#      9999    0.002    0.000    0.002    0.000 simple.py:10(<lambda>)
#         1    0.007    0.007    0.009    0.009 simple.py:4(eratosthenes)
#         1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def simple(n):
    _range = list(range(2, n + 1))
    for i in _range:
        for j in list(range(2, i)):
            if i % j == 0:
                _range[i - 2] = 0
                break
    return list(filter(lambda x: bool(x), _range))

# python3 -m timeit -n 1000 -s "import simple" "simple.simple(10)"
# 1000 loops, best of 5: 7.68 usec per loop

# python3 -m timeit -n 1000 -s "import simple" "simple.simple(100)"
# 1000 loops, best of 5: 143 usec per loop

# python3 -m timeit -n 1000 -s "import simple" "simple.simple(1000)"
# 1000 loops, best of 5: 9.7 msec per loop

# cProfile.run("simple(10000)")
# 10003 function calls in 1.160 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.160    1.160 <string>:1(<module>)
#         1    1.159    1.159    1.160    1.160 simple.py:38(simple)
#      9999    0.001    0.000    0.001    0.000 simple.py:45(<lambda>)
#         1    0.000    0.000    1.160    1.160 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}