# coding=utf-8
import csv

students_list = list()

with open('test_data.csv', encoding="utf-8") as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=',')
    students_list = list(flats_csv)

# print(students_list)

# TODO 1: используя множества, выведите все иностранные языки, которыми владеют студенты (без повторов). например,
#  в таком виде: Английский,Украинский
languages = set()

s = []

for student in students_list:
    s.append(str(student[1]).lower().strip())

s.pop(0)

languages = set(s)

print(languages)

print('')

# TODO 2: у некоторых студентов язык не указан. Сделайте проверку на пустое значение через assert
# не забудьте добавить код перехвата и обработки исключения

for student in students_list:
    try:
        assert student[1] != ''
    except:
        print("Empty language field!")

print('')

# TODO 3: подсчитайте и выведите УНИКАЛЬНЫЕ имена студентов (т.е. те, которые встретились в списке students_list
#  только один раз) например, в таком виде: Кирилл, Максим, Гильтяй,... для неуникальных имен выведите имя и
#  количество повторов. Например:  Андрей, 2 подсказка: решите эту задачу не "в лоб" перебором списка,
#  а другим способом: 1) сделайте множество из имен, 2) используйте его для прохода по списку и подсчета частоты
#  встречаемости имен не забудьте отделить фамилию от имени через string.split()

names_list = []

students_list.pop(0)

for student in students_list:
    names_list.append(student[0].split(' ')[1])

names_set = set(names_list)

for name in names_set:
    print(name + ' ' + str(names_list.count(name)))


