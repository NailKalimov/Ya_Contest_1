"""Дана последовательность слов. вывести все самые короткие слова 
через пробел"""

def find_short_words(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(word)
    answer = []
    # answer = ''
    for word in words:
        if len(word) == minlen:
            answer.append(word)
            # answer += word + " "
    return " ".join(answer)
    # return answer

# P.s. Использование answer:str Делает алгоритм нелинейным по сложности, 
# т.к. в каждой итерации происходит создание нового объекта answer:str