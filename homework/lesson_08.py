#
class Date:
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
                if 2022 >= year >= 0:
                    return f'Верно'
                else:
                    return f'Неверный год'
            else:
                return f'Неверный месяц'
        else:
            return f'Неверный день'

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'


today = Date('20 - 04 - 2022')
print(today)
print(Date.valid(11, 11, 2022))
print(today.valid(10, 13, 2014))
print(Date.extract('11 - 11 - 2022'))
print(today.extract('12 - 12 - 2014'))
print(Date.valid(1, 12, 2002))
#
class Error:
    def __init__(self, txt):
        selfr.txt = txt


a = int(input('Введите делимое >> '))
b = int(input('Введите делитель >> '))
try:
    if b == 0:
        raise Error('Деление на ноль')
except Error as er:
    print(er)
else:
    result = a / b
    print(result)
#
class MyError:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        # self.my_list = [int(i) for i in input('Введите значения через пробел ').split()]
        # value = int(input('Введите значения и нажимайте Enter - '))
        # self.my_list.append(val)
        while True:
            try:
                value = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(value)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = MyError(1)
print(try_except.my_input())
#
class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        # print(f'Для выхода - Q, продолжение - Enter')
        # while True:
        try:
            unit = input(f'Введите наименование >> ')
            unit_p = int(input(f'Введите цену за ед >> '))
            unit_q = int(input(f'Введите количество >>  '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('Epson', 2500, 4, 15)
unit_2 = Scanner('HP', 1500, 8, 6)
unit_3 = Copier('Brother', 3000, 1, 10)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
#
class Complex:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, Complex):
            other = other.__complex

        complex_ = self.__complex + other
        return Complex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, Complex):
            other = other.__complex

        complex_ = self.__complex * other
        return Complex(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


if __name__ == '__main__':
    c1 = Complex(4, -2)
    c2 = Complex(6)

    print(c1 + c2, complex(4, -2) + complex(5))
    print(c1 * c2, complex(4, -2) * complex(5))
#