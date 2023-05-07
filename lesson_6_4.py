# 4. Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f"{self.color} {self.name} started moving")

    def stop(self):
        return print(f"{self.color} {self.name} stopped")

    def turn(self, direction):
        return print(f"{self.color} {self.name} turned {direction}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current speed of town car {self.color} {self.name} is {self.speed}")
        if self.speed > 60:
            print(f"Speed of {self.color} {self.name} is higher than allow for town car")
        else:
            print(f"Speed of {self.color} {self.name} is normal for town car")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current speed of work car {self.color} {self.name} is {self.speed}")
        if self.speed > 40:
            print(f"Speed of {self.color} {self.name} is higher than allow for work car")
        else:
            print(f"Speed of {self.color} {self.name} is normal for work car")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current speed of work car {self.color} {self.name} is {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current speed of work car {self.color} {self.name} is {self.speed}")

    def police(self):
        if self.is_police:
            print(f"{self.color} {self.name} is from police department")
        else:
            print(f"{self.color} {self.name} is not from police department")


if __name__ == "__main__":
    try:
        speed = int(input("Enter speed: "))
        color = input("Enter color: ")
        name = input("Enter name: ")
        direction = input("Enter direction: ")
        Audi = SportCar(speed, color, name, False)
        Audi.go()
        Audi.show_speed()
        Audi.turn(direction)
        Audi.stop()
    except ValueError as e:
        print(e)

    try:
        speed = int(input("Enter speed: "))
        color = input("Enter color: ")
        name = input("Enter name: ")
        direction = input("Enter direction: ")
        Tesla = TownCar(speed, color, name, False)
        Tesla.go()
        Tesla.show_speed()
        Tesla.turn(direction)
        Tesla.stop()
    except ValueError as e:
        print(e)

    try:
        speed = int(input("Enter speed: "))
        color = input("Enter color: ")
        name = input("Enter name: ")
        direction = input("Enter direction: ")
        Toyota = WorkCar(speed, color, name, False)
        Toyota.go()
        Toyota.show_speed()
        Toyota.turn(direction)
        Toyota.stop()
    except ValueError as e:
        print(e)

    try:
        speed = int(input("Enter speed: "))
        color = input("Enter color: ")
        name = input("Enter name: ")
        direction = input("Enter direction: ")
        Ford = PoliceCar(speed, color, name, True)
        Ford.go()
        Ford.show_speed()
        Ford.turn(direction)
        Ford.stop()
        Ford.police()
    except ValueError as e:
        print(e)
