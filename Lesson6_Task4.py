"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Car {self.name}: GO")

    def stop(self):
        print(f"Car {self.name}: STOP")

    def turn(self, direction):
        print(f"Car {self.name}: TURN to {direction}")

    def show_speed(self):
        print(f"Car {self.name}: speed = {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Car {self.name}: Overspeed!")
        else:
            print(f"Car {self.name}: speed = {self.speed}")


class SportCar(Car):
    """"""


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Car {self.name}: Overspeed!")
        else:
            print(f"Car {self.name}: speed = {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


print('---------------------TownCar_1----------------------------')
TownCar_1 = TownCar(55, 'red', 'TownCar_1')
print(TownCar_1.speed, TownCar_1.color, TownCar_1.name, TownCar_1.is_police)
TownCar_1.go()
TownCar_1.turn('right')
TownCar_1.turn('left')
TownCar_1.show_speed()

print('--------------------TownCar_2-----------------------------')
TownCar_2 = TownCar(65, 'green', 'TownCar_2')
print(TownCar_2.speed, TownCar_2.color, TownCar_2.name, TownCar_2.is_police)
TownCar_2.go()
TownCar_2.turn('right')
TownCar_2.turn('left')
TownCar_2.show_speed()

print('------------------------SportCar_1-------------------------')
SportCar_1 = SportCar(65, 'green', 'SportCar_1')
print(SportCar_1.speed, SportCar_1.color, SportCar_1.name, SportCar_1.is_police)
SportCar_1.go()
SportCar_1.turn('right')
SportCar_1.turn('left')
SportCar_1.show_speed()

print('---------------------WorkCar_1----------------------------')
WorkCar_1 = WorkCar(65, 'green', 'WorkCar_1')
print(WorkCar_1.speed, WorkCar_1.color, WorkCar_1.name, WorkCar_1.is_police)
WorkCar_1.go()
WorkCar_1.turn('right')
WorkCar_1.turn('left')
WorkCar_1.show_speed()

print('---------------------PoliceCar_1----------------------------')
PoliceCar_1 = PoliceCar(65, 'green', 'PoliceCar_1')
print(PoliceCar_1.speed, PoliceCar_1.color, PoliceCar_1.name, PoliceCar_1.is_police)
PoliceCar_1.go()
PoliceCar_1.turn('right')
PoliceCar_1.turn('left')
PoliceCar_1.show_speed()
