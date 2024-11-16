"""Бригада скорой помощи выехала по вызову в один из отделенных районов. К 
сожалению, когда диспетчер получил вызов, он успел записать только адрес дома 
и номер квартиры K1, а затем связь прервалась. Однако он вспомнил, что по  
этому же адресу дома некоторое время назад скорая помощь выезжала в квартиру  
K2, которая расположена в подъезда P2 на этаже N2. Известно, что в доме M  
этажей и количество квартир на каждой лестничной площадке одинаково. Напишите  
программу, которая вычисляет номер подъезда P1 и номер этажа N1 квартиры K1.

Формат ввода
Во входном файле записаны пять положительных целых чисел K1, M, K2, P2, N2. 
Все числа не превосходят 10**6. Пример: 89 20 41 1 11

Формат вывода
Выведите два числа P1 и N1. Если входные данные не позволяют однозначно 
определить P1 или N1, вместо соответствующего числа напечатайте 0. Если входные 
данные противоречивы, напечатайте два числа –1 (минус один).
Пример 1
Ввод 89 20 41 1 11	Вывод 2 3
Пример 2
Ввод 11 1 1 1 1	Вывод 0 1
Пример 3
Ввод 3 2 2 2 1	Вывод -1 -1
"""

def calculate_floor_entracne_number(flat_number, floors_in_town, flats_on_floor):
    floors_before = (flat_number - 1) // flats_on_floor
    entrance = floors_before // floors_in_town + 1
    floor = floors_before % floors_in_town + 1
    return entrance, floor


def check_valid(floors_in_town, flat_number, entrance_number, floor_number, flats_on_floor):
    nentrance, nfloor = calculate_floor_entracne_number(
        flat_number, floors_in_town, flats_on_floor)
    if nfloor == floor_number and nentrance == entrance_number:
        return nentrance, nfloor
    return -1, - 1

if __name__ == '__main__':
    MAX_APP_ON_FLOOR = 100
    data = list(map(int, input().split()))
    k1, M, k2, p2, f2 = data[0], data[1], data[2], data[3], data[4]
    goodflag = False
    ent = -1
    floor = -1
    flats_on_floor = -1

    for flats_on_floor in range(1, MAX_APP_ON_FLOOR):
        nentrance, nfloor = check_valid(M, k2, p2, f2, flats_on_floor=flats_on_floor)
        if nentrance != -1:
            goodflag = True
            if ent == -1:
                ent, floor = calculate_floor_entracne_number(flat_number=k1, floors_in_town=M, flats_on_floor=flats_on_floor)
            elif ent != nentrance and ent != 0:
                ent = 0
            elif floor != nfloor and floor != 0:
                floor = 0
    if goodflag:
        print(ent, floor)
    else:
        print('-1 -1')
