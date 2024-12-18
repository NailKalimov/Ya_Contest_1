"""Имеется N кг металлического сплава. Из него изготавливают заготовки массой 
K кг каждая. После этого из каждой заготовки вытачиваются детали массой M кг 
каждая (из каждой заготовки вытачивают максимально возможное количество 
деталей). Если от заготовок после этого что-то остается, то этот материал 
возвращают к началу производственного цикла и сплавляют с тем, что осталось 
при изготовлении заготовок. Если того сплава, который получился, достаточно 
для изготовления хотя бы одной заготовки, то из него снова изготавливают 
заготовки, из них – детали и т.д. Напишите программу, которая вычислит, какое 
количество деталей может быть получено по этой технологии из имеющихся исходно 
N кг сплава.

Формат ввода
Вводятся N, K, M. Все числа натуральные и не превосходят 200.

Формат вывода
Выведите одно число — количество деталей, которое может получиться по такой 
технологии."""


def calc(total_material, one_blank, one_detail):
    if total_material < one_blank or one_blank < one_detail or total_material < one_detail:
        return 0
    else:
        number_of_blank = total_material // one_blank
        number_of_detail_from_blank = one_blank // one_detail
        remains = total_material % one_blank + \
            number_of_blank*(one_blank % one_detail)
        return (
            number_of_blank * number_of_detail_from_blank
            + calc(remains, one_blank, one_detail)
        )


n, k, m = map(int, input().split())
print(calc(n, k, m))
