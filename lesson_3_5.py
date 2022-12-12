# def my_sum():
#     sum_res = 0
#     exit = False
#     while exit == False:
#         number = input('enter a number, if you want to exit enter any letter - ').split()
#         res = 0
#         for i in range(len(number)):
#             if number[i] != 'Q' or number[i] != 'q':
#                 exit = True
#                 break
#             else:
#                 res = res + int(number[i])
#         sum_res = sum_res + res
#         print(f'Current sum is {sum_res}')
#     print(f'Your final sum is {sum_res}')
# my_sum()
# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
# добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу
s = 0
try:
    while True:
        for n in map(int, input('enter a number, if you want to exit enter any letter - ').split()):
            s += n
        print(f'Current sum is {s}')
except ValueError:
    print(f'Your final sum is {s}')
