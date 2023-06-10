# 1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, date_str):
        day, month, year = map(int, date_str.split("-"))
        return f"{day}.{month}.{year}"

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2023 >= year >= 0:
                    return f'All right'
                else:
                    return f'Wrong year'
            else:
                return f'Wrong month'
        else:
            return f'Wrong day'

    def __str__(self):
        return f'The current date {Data.extract(self.day_month_year)}'


today = Data('7 - 01 - 2001')
print(today)
print(Data.valid(11, 11, 2024))
print(today.valid(11, 13, 2011))
print(Data.extract('08 - 11 - 2006'))
print(today.extract('02 - 02 - 2020'))
print(Data.valid(1, 11, 2000))
