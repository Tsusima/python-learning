# 2) Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.


def my_func():
    with open("test_file_5_2.txt", "r") as my_file:
        content = my_file.readlines()
        print(f"Content files:\n{''.join(content)}")
        print("Number of lines:", len(content))
        for i in range(len(content)):
            print(f"Number of characters in the {i + 1} line: {len(content[i])}")
        my_file.seek(0)
        print(f"Total words: {len(my_file.read().split())}")


my_func()
