import time
from turtle import Turtle


class TrafficLight:
    def __init__(self, color):
        self.__color = color
        self.pen1 = Turtle(shape='circle')
        self.pen1.shapesize(5)
        self.pen1.color('black', f"{self.__color}")
        self.pen1.penup()
        self.pen1.sety(190)

        self.pen2 = self.pen1.clone()
        self.pen2.penup()
        self.pen2.sety(0)

        self.pen3 = self.pen1.clone()
        self.pen3.penup()
        self.pen3.sety(-190)
        self.traf()

    def traf(self):
        self.pen1.fillcolor("Red" if self.__color == "Red" else "Black")
        self.pen2.fillcolor("Yellow" if self.__color == "Yellow" else "Black")
        self.pen3.fillcolor("Green" if self.__color == "Green" else "Black")

    def running(self):
        while True:
            if self.__color == "Red":
                time.sleep(7)
                self.__color = "Yellow"
                self.traf()
            elif self.__color == "Yellow":
                time.sleep(2)
                self.__color = "Green"
                self.traf()
            elif self.__color == "Green":
                time.sleep(5)
                self.__color = "Red"
                self.traf()


traffic = TrafficLight("Red")
traffic.running()
