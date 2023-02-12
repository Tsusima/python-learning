# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его
# формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

my_list = []
a = int(input("Enter the number of numbers in the list: "))
for i in range(a):
    b = int(input("Enter list items: "))
    my_list.append(b)
new_list = [my_list[i + 1] for i in range(len(my_list) - 1) if int(my_list[i]) < int(my_list[i + 1])]
print(f"Start List: {my_list}")
print(f"New List: {new_list}")
