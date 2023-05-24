# 2. Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_calculation(self):
        mass = self.__length * self.__width * 25 * 5 / 1000
        return mass


if __name__ == '__main__':
    try:
        length, width = int(input("Enter length: ")), int(input("Enter width "))
        rd = Road(length, width)
        print(f'Need {rd.mass_calculation()} ton for the building')
    except ValueError as e:
        print(e)

# class Road:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def mass_calculation(self):
#         mass = self.length * self.width * 25 * 5 / 1000
#         print(f'Need {mass} ton for the building')


# if __name__ == '__main__':
#     try:
#         length, width = int(input("Enter length: ")), int(input("Enter width "))
#         rd = Road(length, width)
#         rd.mass_calculation()
#     except ValueError as e:
#         print(e)
