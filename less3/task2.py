"""
Во входном файле (вы можете читать данные из sys.stdin, подключив 
библиотеку sys) записан текст. Словом считается последовательность 
непробельных символов идущих подряд, слова разделены одним или большим 
числом пробелов или символами конца строки. Определите, сколько 
различных слов содержится в этом тексте.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.

Пример
Ввод:	
'She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.'
Вывод: 19
"""
import sys


#fast
def fast_quantity_exclusive_elements(data:list):
    dublicate = dict()
    ans = []
    for i in data:
        if dublicate.get(i) == None:
            dublicate[i] = 0
            ans.append(i)
    return len(ans)


#slow
def quantity_exclusive_elements1(data: list):
    ans = []
    for i in range(len(data)):
        if data[i] not in ans:
            ans.append(data[i])
    return len(ans)


#slow
def quantity_exclusive_elements(data: list):
    dublicates = []
    ans = []
    flag = True
    for i in range(len(data)-1):
        if i not in dublicates:
            for j in range(i+1, len(data)):
                if data[i] == data[j]:
                    dublicates.append(j)
            ans.append(data[i])
    return len(ans)


print(fast_quantity_exclusive_elements(data=sys.stdin.read().split()))

