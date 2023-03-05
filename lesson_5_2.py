# 2) Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.


my_file = open("test_file_5_2.txt", "r")
print(f"Content files:\n{my_file.read()}")
my_file = open("test_file_5_2.txt", "r")
print(f"Number of lines in file: {len(my_file.readlines())}")
my_file = open("test_file_5_2.txt", "r")
content = my_file.readlines()
for i in range(len(content)):
    print(f"Number of characters in the {i + 1} line {len(content[i])}")
my_file = open("test_file_5_2.txt", "r")
print(f"Total words: {len(my_file.read().split())}")
my_file.close()
