class Complex:
    def __init__(self, number):
        self.number = number.split()
        self.r = int(self.number[0])
        if self.number[2][0] == "i":
            self.i = int(self.number[1] + "1")
        else:
            if self.number[1] == "-":
                self.i = int(self.number[1] + self.number[2][:-1])
            else:
                self.i = int(self.number[2][:-1])

    def __str__(self):
        return f"{' '.join(self.number)}"

    def __add__(self, other):
        a = self.r + other.r
        b = self.i + other.i
        if b >= 0:
            return Complex(f"{a} + {b}i")
        else:
            return Complex(f"{a} - {abs(b)}i")

    def __mul__(self, other):
        a = self.r * other.r - self.i * other.i
        b = self.r * other.i + other.r * self.i
        if b >= 0:
            return Complex(f"{a} + {b}i")
        else:
            return Complex(f"{a} - {abs(b)}i")


el_1 = Complex("50 - i")
el_2 = Complex("51 + 60i")

print(el_1 * el_2)
print(el_1 + el_2)
