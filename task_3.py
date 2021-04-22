class Cell:
    def __init__(self, x):
        self.cells = int(x)

    def __add__(self, other):
        cells = self.cells + other.cells
        return Cell(cells)

    def __sub__(self, other):
        cells = self.cells - other.cells
        if cells > 0:
            return Cell(cells)
        else:
            return f"It's wrong"

    def __mul__(self, other):
        cells = self.cells * other.cells
        return Cell(cells)

    def __truediv__(self, other):
        cells = self.cells // other.cells
        return Cell(cells)

    def __str__(self):
        return f"Новая клетка: {self.cells}"

    def make_order(self, num_cells):
        output = []
        i = 0
        while i != self.cells:
            i += 1
            if i % num_cells == 0:
                output.append("*\n")
            else:
                output.append("*")
        return "".join(output)


a = Cell(153)
b = Cell(10)

print(a * b)
print(a + b)
print(b - a)
print(a - b)
c = (a / b)
print(c)
print(c.make_order(6))
