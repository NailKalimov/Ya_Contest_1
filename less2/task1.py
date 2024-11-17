"""Дан список. Определите, является ли он монотонно возрастающим(то есть 
верно ли, что каждый элемент этого списка больше предыдущего).
Выведите YES, если массив монотонно возрастает и NO в противном случае.

Пример 1
Ввод	
1 7 9
Вывод
YES"""


def find(s):
    seq = [int(i) for i in s.split()]
    support = seq[0]
    for i in range(1, len(seq)):
        if seq[i] <= support:
            return 'NO'
        support = seq[i]
    return 'YES'


print(find(input()))
