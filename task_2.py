from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def add(self, x):
        pass


class Clothes:
    def __init__(self):
        self.sum = 0
        self.cloth = []

    def add(self, x):
        self.cloth.append(x)

    def common(self):
        sum_cloth = self.sum
        for el in self.cloth:
            sum_cloth += el
        return sum_cloth


class Suit(Cloth):
    def add(self, x):
        return 2 * x + 0.3


class Coat(Cloth):
    def add(self, x):
        return x / 6.5 + 0.5


base = Clothes()
coat_1 = Coat()
suit_1 = Suit()
coat_2 = Coat()

base.add(coat_2.add(10))
base.add(suit_1.add(1))
base.add(coat_1.add(10))
base.add(suit_1.add(2))
base.add(coat_1.add(10))

print(base.common())
