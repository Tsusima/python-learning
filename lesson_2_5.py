my_list = [7, 5, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (для выхода введите число 10000) - "))
while digit != 10000:
    for i in range(len(my_list)):
        if my_list[i] == digit:
            my_list.insert(i + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[i] > digit and my_list[i + 1] < digit:
            my_list.insert(i + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число "))
