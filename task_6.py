from itertools import cycle, count

my_iter_1 = count(5)
my_iter_2 = cycle("abode")
for i in range(10):
    print(f"{next(my_iter_1)} - {next(my_iter_2)}")
