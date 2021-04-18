class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start draw...")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title} began to draw...")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} began to draw...")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} began to draw...")


marker = Handle("marker")
marker.draw()

parker = Pen("parker")
parker.draw()

pencil = Handle("pencil")
pencil.draw()
