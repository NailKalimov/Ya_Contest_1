"""В школе решили на один прямоугольный стол поставить два прямоугольных 
ноутбука. Ноутбуки нужно поставить так, чтобы их стороны были параллельны 
сторонам стола. Определите, какие размеры должен иметь стол, чтобы оба ноутбука 
на него поместились, и площадь стола была минимальна.

Формат ввода
Вводится четыре натуральных числа, первые два задают размеры одного ноутбука, 
а следующие два — размеры второго. Числа не превышают 1000.

Формат вывода
Выведите два числа — размеры стола. Если возможно несколько ответов, выведите 
любой из них (но только один)."""

from sys import stdin


rectangles = [int(i) for i in stdin.readline().rstrip().split()]
rec1 = rectangles[0:2]
rec2 = rectangles[2:4]
possible_tables = [
    [rect1[0] + rect2[0], max(rect1[1], rect2[1])],
    [rect1[1] + rect2[1], max(rect1[0], rect2[0])],
    [rect1[0] + rect2[1], max(rect1[1], rect2[0])],
    [rect1[1] + rect2[0], max(rect1[0], rect2[1])]
]
min_table = possible_tables[0]
min_table_area = min_table[0] * min_table[1]

for table in possible_tables:
    table_area = table[0] * table[1]
    if table_area < min_table_area:
        min_table = table
        min_table_area = table_area
        
print(*(i for i in min_table))
