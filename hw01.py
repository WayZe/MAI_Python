# ==================
# ДЗ №1: простые типы данных, изменяемые и неизменяемые типы, работа со строками, списки

# Задание: сделайте анализ выгрузки квартир с ЦИАН:

# 1) Измените структуру данных, используемую для хранения данных о квартире. Сейчас квартира = список. Сделайте
# вместо этого квартира = словарь следующего вида: flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2],
# "price":flat[11]}. В задании используйте поля: идентификатор квартиры на ЦИАН, количество комнат, тип (новостройка
# или вторичка), стоимость

# 2) Подсчитайте количество новостроек, расположенных у каждого из метро

import csv

# читаем информацию о квартирах в список flats_list
flats_list = list()
with open('output.csv', encoding="utf-8") as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)

# убираем заголовок
header = flats_list.pop(0)

# создаем словарь с информацией о квартирах
subway_dict = {}
for flat in flats_list:
    subway = flat[3].replace("м.", "")
    subway_dict.setdefault(subway, [])

    # TODO 1: добавьте код, который генерирует новую структуру данных с информацией о квартире - словарь вместо списка

    flat_info = {"id": int(flat[0]), "rooms": int(flat[1]), "type": flat[2], "price": int(flat[11])}
    subway_dict[subway].append(flat_info)

# TODO 2: подсчитайте и выведите на печать количество новостроек, расположенных рядом с каждым из метро. Используйте
#  вариант прохода по словарю, который вам больше нравится for k,v in subway_dict: используйте v для анализа значения
#  ваш код... либо for k in subway_dict: используйте subway_dict[k] для анализа значения ваш код...

for key in subway_dict:
    flats = subway_dict[key]
    count = 0
    for flat in flats:
        if flat["type"] == "новостройка":
            count += 1

    if key != "":
        if count == 1:
            print("Около метро " + str(key) + " - " + str(count) + " новостройка")
        elif (count % 10 == 2 or count % 10 == 3 or count % 10 == 4) and count // 10 != 1:
            print("Около метро " + str(key) + " - " + str(count) + " новостройки")
        else:
            print("Около метро " + str(key) + " - " + str(count) + " новостроек")
    else:
        print("Рядом с " + str(count) + " новостройками отсутствует метро")