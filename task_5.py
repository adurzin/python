my_list = [7, 5, 3, 3, 2]

user_input = int(input("Введите элемент рейтинга: "))

if user_input <= my_list[len(my_list) - 1]:
    my_list.append(user_input)
else:
    i = 0
    while user_input <= my_list[i]:
        i += 1
    my_list.insert(i, user_input)

print(my_list)
