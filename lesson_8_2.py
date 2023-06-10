# 2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.


class DivisionByNull:
    def __init__(self, numerator, denominator):
        self.divider = numerator
        self.denominator = denominator

    @staticmethod
    def divide_by_null(numerator, denominator):
        try:
            return f"Division result: {numerator / denominator}"
        except:
            return f"Division by zero is not allowed"


if __name__ == "__main__":
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter denominator: "))
        print(DivisionByNull.divide_by_null(numerator, denominator))
    except ValueError as e:
        print(e)
