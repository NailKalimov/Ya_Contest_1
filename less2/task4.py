"""Дана последовательность чисел длинной N(N>1)
Найти максималньное число в последовательности и второе по величине число
(такое, которое будет максимальным, если вычеркнуть из последовательности 
одно максимальное число)"""

def find_two_max(seq):
    if seq[0]>seq[1]:
        max1=seq[0]
        max2=seq[1]
    else:
        max1=seq[1]
        max2=seq[0]
    for i in range(2,len(seq)):
        if seq[i]>max1:
            max2=max1
            max1=seq[i]
        elif seq[i]>max2:
            max2=seq[i]
    return max1,max2
