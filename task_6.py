def int_func(text):
    answer = []
    for i in range(len(text)):
        if text[i].isascii() and text[i].islower():
            answer.append(chr(ord(text[i][:1]) - 32) + text[i][1:])
        else:
            pass
    return " ".join(answer)


print(int_func(input("Введите несколько слов через пробел в нижнем регистре: ").split()))
