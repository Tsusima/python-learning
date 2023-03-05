# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("test_file_5_4.txt") as my_file:
    data = my_file.read()
en = ['One', 'Two', 'Three', 'Four']
ru = ['Один', 'Два', 'Три', 'Четыре']
for index, word in enumerate(en):
    if word in data:
        data = data.replace(word, ru[index])
print(data)
with open("test_new_file_5_4", "w") as my_file:
    my_file.write(data)