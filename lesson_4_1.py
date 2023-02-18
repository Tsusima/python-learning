# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.

from itertools import count
from itertools import cycle


def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            yield el


def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        yield next(iter)
        i += 1


print(list(my_count_func(start_number=int(input("enter start number: ")), stop_number=int(input("enter stop number: ")))))
print(list(my_cycle_func(my_list=[123, None, False, [1, 2, True, 23], "str"], iteration=int(input("enter iteration: ")))))
