from sys import argv


def salary():
    return float(argv[1]) * float(argv[2]) + float(argv[3])


print(f"Заработная плата сотрудника составила:  {salary()} рублей")
