# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class MYData:
    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2023 >= year >= 0:
                    return f'ОК'
                else:
                    return f'нет такого года'
            else:
                return f'нет такого месяца'
        else:
            return f'нет такого дня'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = MYData('23 - 1 - 2023')
# print(today)
# print(MYData.valid(11, 11, 2022))
print(MYData.extract('10 - 11 - 2010'))
# print(today.extract('11 - 10 - 2022'))

