def func(name, surname, age, city, email, phone):
    return f"name - {name}, surname - {surname}, age - {age}, " \
           f"city - {city}, email - {email}, phone - {phone}"


print(func(name=input("Ваше имя: "),
           surname=input("Фамилия: "),
           age=int(input("Год рождения: ")),
           city=input("Город проживания: "),
           email=input("E-mail: "),
           phone=input("Телефон: ")))
