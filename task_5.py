def my_func(list_1):
    my_sum = 0
    for i in list_1:
        try:
            my_sum += int(i)
        except ValueError:
            return my_sum
        else:
            pass
    return my_sum


answer = 0
my_list = []
print("Введите строку чисел, разделенных пробелом и нажмите Enter.\n"
      "Если вы хотите прекратить работу программы введите символ - q.")
while "q" not in my_list:
    my_list = input().split()
    sum_list = my_func(my_list)
    answer += sum_list
    print(f"{answer}({sum_list})")
