# def my_func(x, y):
#     return round(x ** y, 4)
#
#
# print(my_func(float(input()), int(input())))


def my_func(x, y):
    if y < 0 <= x:
        ans = 1
        for i in range(abs(y)):
            ans = ans / x
        return round(ans, 4)
    else:
        return "Некорректный ввод!"


print(my_func(float(input("Введите положительное действительное число: ")),
              int(input("Введите отрицательное целое число: "))))
