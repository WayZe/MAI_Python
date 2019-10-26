# ==================
# ДЗ №3: функции
# Дедлайн: 04 ноября 18:14
# Результат присылать на адрес nike64@gmail.com

# также прочитайте раздел "Функции" из книги "A byte of Python" (с.59)

# Задание: сделайте анализ возрастного состава группы студентов, используя функции.
# Помните, что а) у некоторых студентов отсутствуют данные по возрасту, б) возраст может быть задан диапазоном, например, 25-35. Поэтому не забывайте обрабатывать ошибки и исключения!

import csv

# помним, что в этот раз мы читаем не список списков, а список словарей!
# ключи в словаре для каждого студента называются по первой строчке из файла student_ages.csv: "Номер в списке", "Возраст"
ages_list = list()
with open('/Users/andreymakarov/Downloads/mai_python_2019/03 Functions/ages.csv', encoding="utf-8") as csvfile:
    ages_dictreader = csv.DictReader(csvfile, delimiter=',')
    ages_list = list(ages_dictreader)

#print(ages_list)

# подсказка: вот так мы можем получить данные из списка словарей
# именно так мы уже делали в коде лекции с квартирами
for al in ages_list:
    print(f'"Номер в списке": {al["Номер в списке"]}, "Возраст": {al["Возраст"]}')
print()

# Задание 1: напишите функцию, которая разделяет выборку студентов на две части: 
# меньше или равно указанного возраста и больше указанного возраста
# вернуться должна пара "Номер в списке, Возраст"
print("ПЕРВАЯ ФУНКЦИЯ")
print()

def filter_students_1(age):
    under_list = list()
    upper_list = list()
    unknownage_count = 0

    # TODO 1: напишите ваш код проверки.
    # не забудьте исключить студентов, у которых возраст не указан, 
    # и подсчитать их количество
    for al in ages_list:
        if al["Возраст"] == "":
            unknownage_count += 1
        else:

            under = 0
            upper = 0
            try:
                under = int(al["Возраст"])
                if under > age:
                    upper_list.append(al)
                else:
                    under_list.append(al)
            except:
                l = al["Возраст"].split("-")
                under = int(l[0])
                upper = int(l[1])
                if under > age:
                    upper_list.append(al)
                if upper < age:
                    under_list.append(al)

    # возвращаем результат из функции:
    return under_list, upper_list, unknownage_count


# вызываем функцию:
und_list, upp_list, unknwncount = filter_students_1(30)
# TODO 2: выведите результат:
print("Ниже 30")
for a in und_list:
    print(a["Номер в списке"], a["Возраст"])
print()

print("Выше 30")
for a in upp_list:
    print(a["Номер в списке"], a["Возраст"])
print()

print("Без возраста")
print(unknwncount)
print()

# Задание 2: улучшите функцию filter_students_1
# напишите функцию, которая принимает переменное количество параметров, каждый из которых может быть необязательным:
# Список и пример передачи параметров: age=30, warn=True, show_average=True
# 1) warn=True (False) - параметр, указывающий, что делать со студентами, которые не указали возраст:
# если возраст не указали значительно большее количество студентов, чем указали, 
# выводите дополнительно предупреждение, что выборка неточная
# 2) show_average=True (False) нужно ли подсчитать и отобразить средний возраст студента.

# все параметры передавайте как **kwargs, т.е. пару "название параметра - значение параметра"
print("ВТОРАЯ ФУНКЦИЯ")
print()

def filter_students_2(**kwargs):
    under_list = list()
    upper_list = list()
    unknownage_count = 0

    # TODO 3: скопируйте сюда текст функции filter_students_1, которую вы написали ранее, 
    # и измените ее так, чтобы она работала с параметрами **kwargs
    _age = kwargs.get("age")

    for al in ages_list:
        if al["Возраст"] == "":
            unknownage_count += 1
        else:

            under = 0
            upper = 0
            try:
                under = int(al["Возраст"])
                if under > _age:
                    upper_list.append(al)
                else:
                    under_list.append(al)
            except:
                l = al["Возраст"].split("-")
                under = int(l[0])
                upper = int(l[1])
                if under > _age:
                    upper_list.append(al)
                if upper < _age:
                    under_list.append(al)

    # TODO 4: получите остальные два параметра по аналогии:
    warn_if_toomany = kwargs.get("warn")
    show_average = kwargs.get("show_average")

    # TODO 5: сделайте проверку. Если значение параметра warn, show_average = True, 
    # выполните соответствующую обработку. Например:
    if warn_if_toomany == True:
    # напишите здесь код проверки и вывод предупреждающего сообщения пользователю
        if unknownage_count > len(ages_list)/2:
            print("Выборка неточная")
            print()
    if show_average == True:
    # напишите здесь код подсчета и вывода среднего значения возраста студентов
        sum = 0
        for al in ages_list:
            if al["Возраст"] != "":
                try:
                    sum += int(al["Возраст"])

                except:
                    l = al["Возраст"].split("-")
                    sum += (int(l[0]) + int(l[1])) / 2
        
        print("Среднее арифметическое: ", sum / (len(ages_list) - unknownage_count))
        print()

    # возвращаем результат из функции:
    return under_list, upper_list, unknownage_count


# вызываем функцию filter_students_2
und_list, upp_list, unknwncount = filter_students_2(age=30, warn=True, show_average=True)

print("Ниже 30")
for a in und_list:
    print(a["Номер в списке"], a["Возраст"])
print()

print("Выше 30")
for a in upp_list:
    print(a["Номер в списке"], a["Возраст"])
print()

print("Без возраста")
print(unknwncount)

