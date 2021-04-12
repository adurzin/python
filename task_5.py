from functools import reduce


def my_func(prev_n, n):
    return prev_n * n


print(reduce(my_func, [i for i in range(100, 1001, 2)]))
