"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки Stationery")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки Pen")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки Pencil")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки Handle")


Pen_1 = Pen('Pen123')
Pen_1.draw()

Pencil_1 = Pencil('Pencil456')
Pencil_1.draw()

Handle_1 = Handle('Handle789')
Handle_1.draw()
