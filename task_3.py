mounth = int(input("Введите месяц в виде целого числа: "))

# Через список:
list_mounth = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

if mounth in list_mounth[0:3]:
    print("winter")
elif mounth in list_mounth[3:6]:
    print("spring")
elif mounth in list_mounth[6:9]:
    print("summer")
elif mounth in list_mounth[9:12]:
    print("autumn")
else:
    print("Такого месяца не существует.")

# Через словарь:
dict_mounth = {
    1: "winter",
    2: "winter",
    3: "spring",
    4: "spring",
    5: "spring",
    6: "summer",
    7: "summer",
    8: "summer",
    9: "autumn",
    10: "autumn",
    11: "autumn",
    12: "winter"
}

print(dict_mounth.get(mounth))
