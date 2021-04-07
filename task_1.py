
def division(var_1, var_2):
    try:
        var_1 / var_2
    except ZeroDivisionError:
        return "Деление на ноль!"
    else:
        return var_1 / var_2


print(division(int(input()), int(input())))
