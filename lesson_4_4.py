# 4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в
# порядке их следования в исходном списке. Для выполнения задания обязательно используйте
# генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

my_list = []
a = int(input("Enter the number of numbers in the list: "))
for i in range(a):
    b = int(input("Enter list items: "))
    my_list.append(b)
new_list = [i for i in my_list if my_list.count(i) == 1]
print(f"Start List: {my_list}")
print(f"New List: {new_list}")
