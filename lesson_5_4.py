# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("test_file_5_4.txt", "r", encoding="utf-8") as my_file:
    with open("test_new_file_5_4.txt", "w", encoding="utf-8") as new_file:
        for line in my_file:
            for key, value in my_dict.items():
                line = line.replace(key, value)
            print(line, end='')
            words = line.split()
            for word in words:
                new_file.write(word + '\n')
