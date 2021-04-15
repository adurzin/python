
lessons = dict()

with open("text_6.txt", "r", encoding="utf-8") as file:
    for line in file:
        number, total = "", 0
        for symbol in line:
            if symbol.isdigit():
                number = number + symbol
            else:
                if number != "":
                    total += int(number)
                number = ""

        lessons[line.split(":")[0]] = total

print(lessons)
