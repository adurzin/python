from random import randint

my_list = [randint(1, 100) for num in range(randint(5, 20))]
print(my_list)

print([my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]])
