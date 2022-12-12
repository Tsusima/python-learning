# Программа принимает действительное положительное число x и целое отрицательное число
# y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
# my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
# числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
# помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.
def my_func(x, y):
    if y <= 0:
        v1 = x ** y
        v2 = 1
        i = 1
        while i <= abs(y):
            v2 *= x
            i += 1
            return v1, 1 / v2
    if y > 0:
        print("You must enter a negative number, please try again")


control = None
try:
    while True:
        control = input("For quit press 'Q', for continue press 'Enter': ").upper()
        if control == 'Q':
            break
        else:

            print(my_func(int(input("enter the positive number you want to raise to a power: ")),
                          int(input("enter a negative number to which the first number will be raised: "))))
except ValueError:
    print('error')
