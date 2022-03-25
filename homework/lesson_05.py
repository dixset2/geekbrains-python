f = open("my_file.txt", "w")
text = input('Введите текст \n')
while text:
    f.writelines(text)
    text = input('Введите текст \n')
    if not text:
        break

f.close()
f = open('my_file.txt', 'r')
content = f.readlines()
print(content)
f.close()
#
#
text = ['Привет\n', 'Как дела?\n', 'Нормально\n']
with open("my_file_2.txt", 'w+') as file_obj:
    file_obj.writelines(text)
with open("my_file_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line) - 1
        print(f"{letters} << Букв в строке ")
    print(f"Количество строк >> {lines}")
#
#
import sys

min_salary = 20000
file = "my_file_3.txt"

if __name__ == "__main__":
    try:
        with open(file, encoding='utf-8') as fh:
            employees = fh.readlines()
    except IOError as e:
        print(e)
        sys.exit(1)

    summ_salary = 0

    for employee in employees:
        name, salary = employee.split()

        try:
            salary = float(salary)
        except ValueError:
            continue

        summ_salary += salary
        if salary < min_salary:
            print(name)

    print('Средний оклад: ', round(summ_salary / len(employees), 2))
#
#
string = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_string = []
with open('my_file_4.txt', 'r') as file_obj:
    # content = file_obj.read().split('\n')
    for i in file_obj:
        i = i.split(' ', 1)
        new_string.append(string[i[0]] + '  ' + i[1])
    print(new_string)

with open('my_file_4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_string)
#
#
def summary():
    try:
        with open('my_file_5.txt', 'w+') as file_obj:
            line = input('Введите числа через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно записаны числа')


summary()
#
#
File = "my_file_6.txt"

subjects = {}

try:
    with open(File, encoding='utf-8') as fh:
        lines = fh.readlines()

    for line in lines:
        data = line.replace('(', ' ').split()

        subjects[data[0][:-1]] = sum(
            int(i) for i in data if i.isdigit()
        )
except IOError as e:
    print(e)
except ValueError:
    print("Введены некорректные данные")

print(subjects)
#