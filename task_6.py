
lessons = dict()

with open("text_6.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.split(":"))
        lessons[line.split(":")[0]] = line.split()

print(lessons)