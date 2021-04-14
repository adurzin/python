from random import randint

total, my_list = 0, [str(randint(0, 10)) for i in range(0, randint(5, 10))]

with open("text_5.txt", "w+", encoding="utf-8") as file:
    file.write(" ".join(my_list))
    file.seek(0)
    for i in file.readline():
        if i != " ":
            total += int(i)

print(f"Сумма чисел в файле = {total}")

