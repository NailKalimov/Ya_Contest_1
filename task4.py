"""Решите в целых числах уравнение:

(ax + b)^0.5 = c 

a, b, c – данные целые числа: найдите все решения или сообщите, что решений в 
целых числах нет.

Формат ввода
Вводятся три числа a, b и c по одному в строке.

Формат вывода
Программа должна вывести все решения уравнения в порядке возрастания, либо NO 
SOLUTION (заглавными буквами), если решений нет. Если решений бесконечно много, 
вывести MANY SOLUTIONS."""

from sys import stdin


a, b, c = (int(i) for i in stdin.readlines())
def find_integer_solutions(a, b, c):
    if c >= 0:
        if a == 0:
            if b**0.5 == c:
                return "MANY SOLUTIONS"
            elif b**0.5!= c:
                return "NO SOLUTION"
        elif a !=0:
            x = (c**2-b)/a
            if x.is_integer(): #and x >= -b/a:
                return int(x)
    return "NO SOLUTION"
    
print(find_integer_solutions(a, b, c))
