"""
В списке хранятся числа. Найти два различных числа A и B, сумма которых равна x
или вернуть пару 0 0, если таких чисел нет.
"""

# O(n^2)
def slow_find(lst: list, x):
    for a in lst:
        for b in lst:
            if a+b == x and a != b:
                return a, b
    return 0, 0


def slow_find(lst: list, x):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == x:
                return lst[i], lst[j]
    return 0, 0

# O(n)
def fast_search(lst: list, x):
    processed_num = set()
    for a in lst:
        if (x - a) in processed_num:
            return a, x-a
        else:
            processed_num.add(a)
    return 0, 0
