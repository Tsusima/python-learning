# 1) Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.


my_file = open("test.txt", "w")
line = input("Enter text, if you dont want to enter anything else press Enter: ")
while line:
    my_file.writelines(line)
    line = input("Enter text, if you dont want to enter anything else press Enter: ")
    if not line:
        break

my_file.close()
with open("test.txt", "r") as my_file:
    print(my_file.readlines())

