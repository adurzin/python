class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, bonus, wage):
        super().__init__(name, surname, position, bonus, wage)
        self._income = {"wage": wage, "bonus": bonus}
        print(self.name, self.surname, self.position, self._income)

    def get_full_name(self):
        print(f"Full name: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Total income: {self._income['bonus'] + self._income['wage']}")


prezident = Position("Boris", "Tkachev", "prezident", 100000, 30000)
administrator = Position("Pavel", "Derevyanko", "administrator", 5000, 1000)

prezident.get_full_name()
prezident.get_total_income()
administrator.get_full_name()
administrator.get_total_income()

