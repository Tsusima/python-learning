print("Задание №1")
a = 0
b = 1
print("Переменные a и b - ", a, b)
stroka = input("Введите первую строку ")
chislo = int(input("Введите первое число "))
stroka1 = input("Введите вторую строку ")
chislo1 = int(input("Введите второе число "))
print(stroka, chislo)
print(stroka1, chislo1)

print("Задание №2")
time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")
print("")
print("Задание №3")

n = int(input("Введите число"))
symma = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(symma)

print("Задание №4")
aa = int(input("Введите целое положительное число"))
bb = 0
while aa > 0:
    x = aa % 10
    if x >= bb:
        bb = x
    aa //= 10
print("Максимальное цифра в числе", bb)

print("Задание №5")
profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print("Фирма работает с прибылью. Рентабельность выручки составила", profit / costs)
    workers = int(input("Введите количество сотрудников фирмы"))
    print("прибыль в расчете на одного сторудника сотавила", profit / workers)
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

print("Задание №6")
den1 = int(input("Введите результаты пробежки  спортсменна в первый день"))
denx = int(input("Введите желаемый результат пробежки"))
kolvo_dney = 1
kolvo_km = den1
while den1 <= denx:
    den1 = den1 + den1 * 0.1
    kolvo_dney += 1
    kolvo_km += den1
print("День в котором спортсмен достигнет желаемого результата", kolvo_dney)
