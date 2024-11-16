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
if lst[0] >= lst[1]: # make sure that m1 != m2 and s1 != s2
    m1, m2 = lst[0], lst[1]
    s1, s2 = lst[0], lst[1]
elif lst[0] < lst[1]:
    m1, m2 = lst[1], lst[0]
    s1, s2 = lst[1], lst[0]

for i in lst:
    # maximum and second maximum
    if i > m1:
        m1, m2 = i, m1
    elif i > m2:
        m2 = i
    # minimum and second minimum
    if i < s1:
        s1, s2 = i, s1
    elif i < s2:
        s2 = i
if len(lst) == 2:
    print(" ".join(str(i) for i in sorted(lst)))
elif m1 * m2 > s1 * s2:
    print(" ".join(str(i) for i in sorted([m1, m2])))
else:
    print(" ".join(str(i) for i in sorted([s1, s2])))
