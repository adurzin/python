import json

my_dict = dict()
average_profit, count = 0, 0
my_list = [my_dict, None]

with open("text_7.txt", "r", encoding="utf-8") as file:
    for line in file:
        profit = int(line.split()[2]) - int(line.split()[3])
        if profit > 0:
            count += 1
            average_profit += profit
        my_dict[line.split()[0]] = profit
    my_list[1] = {"average_profit": average_profit / count}

    with open("text_77.json", "w", encoding="utf-8") as data:
        json.dump(my_list, data, indent=4, ensure_ascii=False)
