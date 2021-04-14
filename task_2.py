
with open("example.txt", "r", encoding="utf-8") as file:
    i = 0
    for line in file:
        i += 1
        j = 0
        for word in line.split():
            j += 1
        print(f"в {i} строке {j} слов(а)")
    print(f"всего в файле {i} строк(и)")
