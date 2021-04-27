class Division(Exception):
    def __init__(self, txt):
        self.txt = txt


el_1, el_2 = input("Enter number: "), input("Enter second number: ")

try:
    el_1, el_2 = int(el_1), int(el_2)
    if el_2 == 0:
        raise Division("Division by Zero!")
except ValueError:
    print("Incorrect enter numbers!")
except Division as err:
    print(err)
else:
    print(el_1 / el_2)
