list_1 = input("Введите элементы списка через пробел: ").split()

for i in range(1, len(list_1), 2):
    list_1[i], list_1[i - 1] = list_1[i - 1], list_1[i]

print(list_1)
