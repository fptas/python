
from abc import ABC, abstractmethod

class Сlothes(ABC):
    def __init__(self, value):
        self.value = value
    @abstractmethod
    def Calc(self):
        pass


class Coat(Сlothes):
    @property
    def V(self):
        return self.value
    @V.setter
    def V(self, v):
        self.value = v
    def Calc(self):
        return self.V / 6.5 + 0.5


class Suit(Сlothes):
    @property
    def H(self):
        return self.value
    @H.setter
    def H(self, h):
        self.value = h
    def Calc(self):
        return 2 * self.H + 0.3

coat_1 = Coat(50)
print(coat_1.V)
print(coat_1.Calc())
coat_1.V = 52
print(coat_1.Calc())
print("----------------------------------")
suit_1 = Suit(4)
print(suit_1.H)
print(suit_1.Calc())
suit_1 = Suit(3)
print(suit_1.Calc())
