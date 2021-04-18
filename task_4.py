class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} went...")

    def stop(self):
        print(f"{self.name} stopped!")

    def turn(self, direction):
        print(f"{self.name} turned to {direction}...")

    def show_speed(self):
        print(f"Your speed: {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Speed was disrupted!")
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Speed was disrupted!")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


ford = PoliceCar(60, "blue", "Mustang")
print(ford.speed, ford.name, ford.is_police, ford.color)
ford.show_speed()
ford.go()
ford.turn("left")
ford.stop()

uaz = WorkCar(41, "green", "Patriot")
uaz.show_speed()
print(uaz.is_police)
uaz.go()
uaz.turn("right")
uaz.stop()

toyota = TownCar(50, "red", "Camry", False)
toyota.show_speed()
print(toyota.is_police)
toyota.go()
toyota.turn("me")
toyota.stop()


audi = SportCar(100, "black", "Q7", False)
audi.show_speed()
print(audi.is_police)
audi.go()
audi.turn("me")
audi.stop()
