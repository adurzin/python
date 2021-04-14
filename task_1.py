
with open("example.txt", "w+", encoding="utf-8") as file:
    while True:
        txt = input()
        if txt == "":
            break
        file.writelines(f"{txt}\n")
