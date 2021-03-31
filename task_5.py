earnings = int(input("Введите количество выручки предприятия: "))
cost = int(input("Введите количество издержек предприятия: "))

if earnings > cost:
    profit = (earnings - cost) / earnings
    print(f"Предприятие прибыльное, рентабельность бизнеса - {profit:.2f}")
    size = int(input("Введите количество сотрудников предпрятия: "))
    gain = (earnings - cost) / size
    print(f"Ваша прибыль фирмы в расчете на каждого сотрудника: {gain:.1f} млн. руб.")
elif earnings < cost:
    print("Предприятие сработало в убыток")
else:
    print("Предприятие сработало без прибыли и без убытка")
