# 5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


def summary():
    try:
        with open("test_file_5_5.txt", "w+") as my_file:
            line = input("Enter data separated by a space: ")
            my_file.writelines(line)
            my_numb = line.split()
            print(f"The sum of the numbers in the file: {sum(map(int, my_numb))}")
    except IOError:
        print("File error")
    except ValueError:
        print("Number dialed incorrectly. I/O error")


summary()