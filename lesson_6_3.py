# 3. Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = (f"{self.name} {self.surname}")
        return full_name

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


if __name__ == "__main__":
    try:
        name, surname, position, wage, bonus = input("Enter your name: "), input("Enter your surname: "), input(
            "Enter your position: "), int(input("Enter your wage: ")), int(input("Enter your bonus: "))
        pt = Position(name, surname, position, wage, bonus)
        print(f"Full name: {pt.get_full_name()}")
        print(f"Total income: {pt.get_total_income()}")

    except ValueError as e:
        print(e)

        
     
# class Worker:

#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}


# class Position(Worker):

#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)

#     def get_full_name(self):
#         return print(f"Full name: {self.name} {self.surname}")

#     def get_total_income(self):
#         return print(f"Total income: {self._income.get('wage') + self._income.get('bonus')}")


# if __name__ == "__main__":
#     try:
#         name, surname, position, wage, bonus = input("Enter your name: "), input("Enter your surname: "), input(
#             "Enter your position: "), int(input("Enter your wage: ")), int(input("Enter your bonus: "))
#         pt = Position(name, surname, position, wage, bonus)
#         pt.get_full_name()
#         pt.get_total_income()
#     except ValueError as e:
#         print(e)
