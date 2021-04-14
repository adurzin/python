
with open("text_3.txt", "r", encoding="utf-8") as file:
    total = 0
    count = 0
    person = []
    for line in file:
        count += 1
        total += float(line.split()[1])
        if float(line.split()[1]) < 20000.0:
            person.append(line.split()[0])
    print(f"Сотрудники с доходом менее 20 тыс. руб.: {person}")
    print(f"Средняя величина дохода сотрудников: {total/count}")
