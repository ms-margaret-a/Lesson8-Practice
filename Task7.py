# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class MYComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.n = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма чисел n1 и n2: ')
        return f'n = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение числе n1 и n2:')
        return f'n = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'n = {self.a} + {self.b} * i'


n_1 = MYComplexNumber(5, -4)
n_2 = MYComplexNumber(5, 7)
print(n_1)
print(n_1 + n_2)
print(n_1 * n_2)