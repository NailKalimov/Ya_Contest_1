"""
Дан список, заполненный произвольными целыми числами. Найдите в этом 
списке два числа, произведение которых максимально. Выведите эти числа 
в порядке неубывания.

Список содержит не менее двух элементов. Числа подобраны так, что ответ 
однозначен.

Решение должно иметь сложность O(n), где n - размер списка.
Пример 2
Ввод -4 3 -5 2 5
Вывод -5 -4
"""

lst = list(map(int, input().split()))
if lst[0] >= lst[1]:
    max1, max2 = lst[0], lst[1]
    min1, min2 = lst[1], lst[0]
elif lst[0] < lst[1]:
    max1, max2 = lst[1], lst[0]
    min1, min2 = lst[0], lst[1]

for i in lst:
    if i > max1:
        max1, max2 = i, max1
    elif i > max2:
        max2 = i
    if i < min1:
        min1, min2 = i, min1
    elif i < min2:
        min2 = i
if len(lst) == 2:
    print(" ".join(str(i) for i in sorted(lst)))
elif max1 * max2 > min1 * min2:
    print(" ".join(str(i) for i in sorted([max1, max2])))
else:
    print(" ".join(str(i) for i in sorted([min1, min2])))
