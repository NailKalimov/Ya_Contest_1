"""Дана последовательность N чисел. Найти правое вхождение числа x. Если 
число не встречалось, вывести -1."""


def find(sequence, x):
    answer = -1
    for i in range(len(sequence)):
        if sequence[i] == x:
            answer = i
    return answer


print(find([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
