# def my_func(arg1, arg2, arg3):
#     if arg1 >= arg2 and arg2 >= arg3:
#         return arg1 + arg2
#     elif arg1 >= arg2 and arg2 <= arg3:
#         return arg1 + arg3
#     elif arg1 <= arg2 and arg1 <= arg3:
#         return arg2 + arg3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов
def my_finc():
    my_list = []
    exite = False
    while exite == False:
        try:
            a = int(input("enter a number, if you want to exit enter any letter: "))
        except ValueError:
            exite = True
        my_list.append(int(a))
    del my_list[-1]
    my_list = sorted(my_list)
    s = 0
    for i in range(-1, -6, -1):
        s += int(my_list[i])
    print(s)


my_finc()

# my_list = []
# s = '1234567890qQ'
# exite = True
# while exite == True:
#     c = input("enter a number, if you want to exit enter any letter: ")
#     for x in c:
#         if x not in s:
#             exite = False
#             break
#     if 'q' in c or 'Q' in c:
#         exite = False
#         break
#     else:
#         my_list.append((int(c)))
# my_list = sorted(my_list)
# s = 0
# for i in range(-1, -6, -1):
#     s += int(my_list[i])
# print(s)