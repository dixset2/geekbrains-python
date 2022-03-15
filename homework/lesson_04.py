###

from sys import argv

if len(argv) > 1:
    name_script, time_work, rate, bounty = argv
    time_work = int(time_work)
    rate = int(rate)
    prize = int(bounty)
    print((time_work * rate) + prize)
else:
    time_work = int(input("Введите кол-во часов >> "))
    rate = int(input("Введите ставку >> "))
    bounty = int(input("Введите начисляемую премию >> "))
    print((time_work * rate) + bounty)

###

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list_a = [int(i) for i in my_list]
for i in range(1, len(my_list_a)):
    if my_list_a[i] > my_list[i - 1]:
        print(my_list_a[i], end=' ')

print([x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0])

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_new_list)

###

from functools import reduce


def multiply(prev_el, el):
    return prev_el * el


result = reduce(multiply, [x for x in range(99, 1001) if x % 2 == 0])
print(result)

###

from itertools import count, cycle
from time import sleep

first_number = int(input('Введите первое число >> '))
last_number = int(input('Введите последнее число >> '))
number_gen = (el for el in count(first_number))
for el in number_gen:
    if el <= last_number:
        sleep(1)
        print(el)
    else:
        sleep(1)
        break

###

new_list = input('Введите числа через пробел >>')
list_length = int(input('Укажите длину последовательности >> '))
new_list = new_list.split(' ')
i = 0

new_list_gen = (el for el in cycle(new_list))
for el in new_list_gen:
    if i < list_length:
        sleep(1)
        i += 1
        print(el)
    else:
        sleep(1)
        print('Конец последовательности')
        break

###

def fact(n):
    for el in list(range(1, n + 1)):
        if el == 1:
            result = el
            yield result
        else:
            result = result * el
        yield result


n = int(input('Введите число >> '))
for el in fact(n):
    print(el)
###