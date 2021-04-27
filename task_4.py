from abc import abstractmethod, ABC


class NotStr(Exception):
    def __init__(self, txt):
        self.txt = txt


class Base:
    def __init__(self):
        self.base = {"Printer": [],
                     "Computer": [],
                     "Laptop": []}

    def add_equipment(self, equip, number):
        self.base[equip.__class__.__name__].append(f"{equip.__str__()}. Quantity: {number}")
        return self.base

    def __str__(self):
        return f"{self.base}"


class Equipment(ABC):
    @abstractmethod
    def __init__(self, name, length, width, height):
        try:
            if f"{length}".isdigit() and f"{width}".isdigit() and f"{height}".isdigit():
                self.name = name
                self.length = length
                self.width = width
                self.height = height
            else:
                raise NotStr(f"Need enter correct attribute in class {name}!")
        except NotStr as err:
            print(err)


class Printer(Equipment):
    def __init__(self, name, length, width, height, num_sheets):
        super().__init__(name, length, width, height)
        self.num_sheets = num_sheets

    def __str__(self):
        return f"Name: {self.name}, l: {self.length}mm, w: {self.width}mm," \
               f"h: {self.height}mm, max_sheets: {self.num_sheets} p."


class Laptop(Equipment):
    def __init__(self, name, length, width, height, battery_power):
        super().__init__(name, length, width, height)
        self.battery_power = battery_power

    def __str__(self):
        return f"Name: {self.name}, l = {self.length}mm, w = {self.width}mm," \
               f"h = {self.height}mm, battery power:{self.battery_power}"


class Computer(Equipment):
    def __init__(self, name, length, width, height, power):
        super().__init__(name, length, width, height)
        self.power = power

    def __str__(self):
        return f"Name: {self.name}, l = {self.length}mm, w = {self.width}mm," \
               f"h = {self.height}mm, power:{self.power}"


computer_intel = Computer("Intel", 300, "abc", "350", 650)
computer_amd = Computer("AMD", 200, 100, 230, 800)
laptop_hp = Laptop("HP", 100, 20, 10, 2000)
printer_hp = Printer("HP", 100, 50, 100, 300)
printer_dell = Printer("Dell", 100, 20, 10, 2000)
base = Base()
base.add_equipment(printer_dell, 1)
base.add_equipment(computer_amd, 4)
base.add_equipment(printer_hp, 10)
base.add_equipment(laptop_hp, 3)
print(base)
