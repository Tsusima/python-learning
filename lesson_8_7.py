# # 7) Реализовать проект «Операции с комплексными числами».
# # Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# # Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# # Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + other.real * self.imag)

    def __str__(self):
        if self.imag < 0:
            return f"{self.real} - {-self.imag}i"
        else:
            return f"{self.real} + {self.imag}i"



z1 = ComplexNumber(3, 2)
z2 = ComplexNumber(1, -4)
print("Сумма:", z1 + z2)
print("Произведение:",z1 * z2)
