#
def division(a, b):
    if b != 0:
        return a / b
    else:
        return float('nan')


number1 = float(input('Введите значение a: '))
number2 = float(input('Введите значение b: '))
print('Результат деления: ', division(number1, number2))
#

#
def division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "Деление на ноль невозможно"


print(division(int(input("Введите значение a = ")),
               int(input("Введите значение b = "))))
#

#
def info(name, surname, birthday, city, email, phone):
    function_string = f'Информация о пользователе: Имя: "{name}", Фамилия: "{surname}", Дата рождения: "{birthday}", Город: "{city}", ' \
                      f'Электропочта: "{email}", Телефон: "{phone}"'
    print(function_string)


info(phone='+79116313322', surname='Ли', name='Максим', birthday='22.01.1998', city='Севастополь',
     email='geekbrains@mail.ru')
#

#
def my_func(arg_1, arg_2, arg_3):
    list = [arg_1, arg_2, arg_3]
    total = []
    max_1 = max(list)
    total.append(max_1)
    list.remove(max_1)
    max_2 = max(list)
    total.append(max_2)
    print(sum(total))


my_func(5, 10, 0)
#

#
def my_func(x, b):
    return 1 / x ** abs(b)


print(my_func(2, -5))
#

#
total = 0
calculating = True
while calculating:
        l1 = input("Введите число или спец.символ 'e' для выхода ==")
        for l1 in l1.split():
            if l1.lower() == 'e':
                calculating = False
                break
            total += float(l1)
        print(total)
#
#
def int_func(*args):
    words = input("Введите ваши слова ")
    print(words.title())
    return


int_func()
#