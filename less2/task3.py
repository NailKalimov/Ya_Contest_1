"""Дана последовательность чисел длинной N(N>0). Найти максимальное 
число в последовательности"""


def find_max(seq: list) -> int:
    answer = seq[0]
    for i in seq:
        if i > answer:
            answer = i
    return answer


def fast_find_max(seq: list) -> int:
    answer = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[answer]:
            answer = i  # Запись значения в переменную answer медленнее, чем запоминание его индекса
    return seq[answer]


print(find_max([1, 2, 3, 4, 5]))
