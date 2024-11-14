"""Найти минимальное четное число в списке или -1, если такого нет."""

def min_even(lst):
    answer = -1
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and (answer == -1 or lst[i] < answer):
            answer = lst[i]
    return answer

def find_min_even(lst):
    meeted_even = False
    answer = -1
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and (not meeted_even or lst[i] < answer):
            meeted_even = True
            answer = lst[i]
    return answer

def find_min_even1(lst):
    meeted_even = False
    answer = -1
    for number in lst:
        if number % 2 == 0 and (not meeted_even or number < answer):
            meeted_even = True
            answer = number
    return answer