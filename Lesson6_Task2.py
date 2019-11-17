"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:

    def __init__(self, length, width, weight, thickness):
        self._length = length
        self._width = width
        self._weight = weight
        self._thickness = thickness

    def Calc(self):
        print(f"Total weight: {self._length}m * {self._width}m * {self._weight}kg * {self._thickness}cm = {self._length * self._width * self._weight * self._thickness / 1000} t ")


Road_1 = Road(20, 5000, 25, 5)
Road_1.Calc()

Road_2 = Road(30, 2000, 30, 10)
Road_2.Calc()