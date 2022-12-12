# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.
def personal_info(name, surname, year, city, email, phone):
    return ' '.join(
        ["1)name:", name, "2)surname:", surname, "3)year:", year, "4)city:", city, "5)email:", email, "6)phone:",
         phone])


name2 = input("Input name: ")
surname2 = input("Input surname: ")
year2 = input("Input year: ")
city2 = input("Input city: ")
email2 = input("Input email: ")
phone2 = input("Input phone: ")

print(personal_info(name=name2, surname=surname2, year=year2, city=city2, email=email2, phone=phone2))
