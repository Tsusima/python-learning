# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.
def division():
    try:
        a = float(input("enter the dividend: "))
        b = float(input("enter divisor: "))
    except ValueError:
        return "error"
    if b != 0:
        print(f"result: {a / b}")
    elif b == 0:
        print("undefined")
    return division()


control = None
while True:
    control = input("For quit press 'Q', for continue press 'Enter' ").upper()
    if control == 'Q':
        break
    else:
        division()

    print(division())
