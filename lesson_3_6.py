# def int_func():
#     word = input("Input words: ")
#     print(word.title())
#     return
#
#
# int_func()

# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# © geekbrains.ru 23
# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
# пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
# исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
# написанную ранее функцию int_func().
def my_func(a):
    separate_word = a.split(' ')
    total = []
    for i in separate_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return print(*total)
my_func(input("Input words: "))