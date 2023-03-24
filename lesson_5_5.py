# 5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
import random


def summary():
    with open("test_file_5_5.txt", "w") as my_file:
        for i in range(10):
            number = random.randint(1, 100)
            my_file.write(str(number) + ' ')
    with open("test_file_5_5.txt", "r") as my_file:
        sum_numbers = my_file.read().split()
        print(f"The sum of the numbers in the file: {sum(map(int, sum_numbers))}")


summary()
