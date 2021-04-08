def func(var_1, var_2, var_3):
    ls = [var_1, var_2, var_3]
    n_1 = max(ls)
    ls.remove(max(ls))
    return max(ls) + n_1

print(func(int(input()), int(input()), int(input())))
