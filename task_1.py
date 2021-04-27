class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extract(cls, obj):
        try:
            return [int(i) for i in obj.date.split("-")]
        except ValueError:
            return "Enter correct date..."

    @staticmethod
    def check(self):
        x = self.extract(self)
        try:
            if 1 <= x[0] <= 31 and 1 <= x[1] <= 12 and 0 <= x[2] <= 2021:
                return "It's ok"
            else:
                return "Enter correct date..."
        except ValueError:
            return "Enter correct date..."


my_date_1 = Date("11-12-2022")
print(Date.extract(my_date_1))
print(my_date_1.check(my_date_1))
