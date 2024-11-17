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
def quantity_exclusive_elements(data: list):
    dublicates = []
    ans = []
    flag = True
    for i in range(len(data)):
        if i not in dublicates:
            for j in range(i+1, len(data)):
                if data[i] == data[j]:
                    dublicates.append(j)
            ans.append(data[i])
    return len(ans)


#slow
def quantity_exclusive_elements1(data: list):
    ans = []
    for i in range(len(data)):
        if data[i] not in ans:
            ans.append(data[i])
    return len(ans)


print(fast_quantity_exclusive_elements(data=sys.stdin.read().split()))

