# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.

from sys import argv

if len(argv) > 1:
    name_script, time_work, rate_per_hour, bonus = argv
    time_work = int(time_work)
    rate_per_hour = int(rate_per_hour)
    bonus = int(bonus)
    print((time_work * rate_per_hour) + bonus)
else:
    time_work = int(input("Enter time work: "))
    rate_per_hour = int(input("Enter rate per hour: "))
    bonus = int(input("Enter bonus: "))
    print(f"salary: {(time_work * rate_per_hour) + bonus}")
