class Check(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    enter = input("Enter number or 'stop': ").lower()
    if enter == "stop":
        print(my_list)
        break
    else:
        try:
            if enter.isdigit():
                my_list.append(enter)
            else:
                raise Check("Need enter number... Try again.")
        except Check as err:
            print(err)
