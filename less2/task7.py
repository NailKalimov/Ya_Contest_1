"""Дана строка(возможно, пустая), состоящая из букв A-Z:
AAAABBBCCYZDDDDEEEEFFFFFGGAAAAAAAABBBBBBBBB

Нужно написать функцию, которая на выходе даст строку вида:
A4B3C2YZD4E4F5G2A8B9
Т.е. если символ встречается 1 раз, то он не изменяется, если встречается 
несколько раз, то после его первого вхождения указывается количество повторений"""

def easypeasy(string):
    last_symbol = string[0]
    answer = []
    for i in string:
        if i != last_symbol:
            answer.append(last_symbol)
            last_symbol = i
    answer.append(last_symbol)
    return "".join(answer) # 'AAAAAAAAABBBBBBBBBBBBCDGGGGGGGGGG' -> 'ABCDG'


def pack(char, count):
    if count > 1:
        return char + str(count) # 'AAAAAA' -> 'A5'
    return char 

def RLE(string):
    previous_simbol = string[0]
    simbol_counter = 0
    answer = []
    for i in range(len(string)):
        if string[i] != previous_simbol:
            answer.append(pack(previous_simbol, simbol_counter))
            previous_simbol = string[i]
            simbol_counter = 1
        else:
            simbol_counter += 1
    answer.append(pack(previous_simbol, simbol_counter))
    return "".join(answer)