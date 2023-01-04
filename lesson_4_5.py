# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В
# список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить
# результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce()

from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(f"product of even numbers in the range from 100 to 1000 inclusive: {reduce(my_func, my_list)}")
