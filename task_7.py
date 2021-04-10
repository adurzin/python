def fact(num):
    x = 1
    c = 1
    for i in range(1, num + 1):
        x *= i
        yield f"{c}! = {x}"
        c += 1


n = int(input("Факториалы до какого числа вы хотели бы узнать? "))
for el in fact(n):
    print(el)
