# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        super().__init__(height)

    def fabric_consumption(self):
        return round(2 * self.size + 0.3, 2)


class FabricCalculator:
    def __init__(self, clothes):
        self.clothes = clothes

    @property
    def total_fabric_consumption(self):
        total = 0
        for item in self.clothes:
            total += item.fabric_consumption()
        return round(total, 2)


coat1 = Coat(46)
coat2 = Coat(50)
suit1 = Suit(170)
suit2 = Suit(180)
print(
    f"First coat: {coat1.fabric_consumption()} \nSecond coat: {coat2.fabric_consumption()} \nFirst suit: {suit1.fabric_consumption()} \nSecond suit: {suit2.fabric_consumption()} \nTotal fabric consumption: {FabricCalculator([coat1, coat2, suit1, suit2]).total_fabric_consumption}")
