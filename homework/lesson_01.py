# a = 12
# b = 22
# print("Переменные a и b -", a, b)
# str1 = input("Введите первую строку")
# number1 = int(input("Введите первое число"))
# str2 = input("Введите вторую строку")
# number2 = int(input("Введите второе число"))
# print("Введенные вами значения - %10s %5d %10s %5d" % (str1, number1, str2, number2))

# time = int(input("Введите время в секундах >>>"))
# hours = time // 3600
# minutes = (time-hours * 3600) // 60
# seconds = time - hours * 3600 + minutes * 60
# print(f"Время в чч:мм:cc {hours}:{minutes}:{seconds}")

# n = int(input("Введите ваше число n >>>"))
# sum = (n+ int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
# print("Сумма чисел n + nn + nnn равняется %d" % sum)

# number = abs(int(input("Введите ваше целое положительное число >>>")))
# max = number % 10
# while number >= 1:
#     number = number // 10
#     if number % 10 > max:
#         max = number % 10
#     if number > 9:
#         continue
#     else:
#         print("Максимальная цифра в данном числе ", max)
#         break

# profit = float(input("Введите вашу выручку фирмы >>>"))
# costs = float(input("Введите ваши издержки фирмы >>>"))
# if profit > costs:
#     print(f"Фрима работает с прибылью. Рентабельность выручки составляет {profit / costs:.2f}")
#     workers = int(input("Введите количество сотрудников фирмы >>>"))
#     print(f"Прибыль в расчете на одного сотрудника составляет {profit / workers:2f}")
# elif profit == costs:
#     print("Фирма работает в ноль")
# else:
#     print("Фирма работает в убыток")

# a = int(input("Введите результаты пробежки за первый день в км >>>"))
# b = int(input("Введите общий желаемый результат в км >>>>"))
# result_days = 1
# result_km = a
# while result_km < b:
#     a = a + 0.1 * a
#     result_days += 1
#     result_km = result_km + a
# print(f"Вы достигнете требуемых показателей на %.d день" % result_days)