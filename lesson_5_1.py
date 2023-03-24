# 1) Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

def my_func():
    with open("test.txt", "w",   encoding='utf-8') as my_file:
        while True:
            line = input("Enter text, if you dont want to enter anything else press Enter: ")
            my_file.writelines(line + '\n')
            if not line:
                break


my_func()
