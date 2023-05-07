# 1. Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# © geekbrains.ru 18
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.
from time import sleep


class TrafficLight:
    __states = {'red': 7, 'yellow': 2, 'green': 10}
    __color = ""

    def running(self, repeat):
        self.repeat = repeat
        if repeat == 0:
            for color, time in self.__states.items():
                self.__color = color
                print(f"TrafficLight switched to state {self.__color} on {time} seconds")
                sleep(time)
                print(
                    f"TrafficLight leave state {self.__color} after {time} seconds")
        else:
            for i in range(repeat - 1):
                for color, time in self.__states.items():
                    self.__color = color
                    print(f"TrafficLight switched to state {self.__color} on {time} seconds")
                    sleep(time)
                    print(
                        f"TrafficLight leave state {self.__color} after {time} seconds")


if __name__ == '__main__':
    tl = TrafficLight()
    try:
        repeat = int(input(
            "Enter a natural number to indicate the number of repetitions of the program, otherwise the program will be executed only 1 time: "))
        tl.running(repeat)
    except ValueError:
        print("You have entered an invalid value! The program will be executed 1 time!")
    tl.running(0)
