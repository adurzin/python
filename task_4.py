n = int(input("Введите целое положительное число: "))

maximum = 0

while n:
    m = n % 10
    if m > maximum:
        maximum = m
    n = n // 10

print(f"Самая большая цифра в Вашем числе - {maximum}")
