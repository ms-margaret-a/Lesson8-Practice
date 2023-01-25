# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MYNullDivision:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"На ноль делить нельзя")


div = MYNullDivision(10, 100)
# print(MYNullDivision.divide_by_null(10, 0))
print(MYNullDivision.divide_by_null(10, 0.1))
# print(MYNullDivision(100, 0))
