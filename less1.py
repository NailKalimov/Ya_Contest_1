from sys import stdin

trans = str.maketrans({'+': None,
                       "(": None,
                         ")": None,
                           "-": None,
                             "\n": None})
new_number = stdin.readline().rstrip().translate(trans)
phone_book = [i.translate(trans) for i in stdin.readlines()]
print('new number: ' + new_number)
print('book:', phone_book)
if len(new_number) == 7:
    for number in phone_book:
        if new_number in number:
            if new_number == number:
                print('YES')
            elif new_number == number[4:] and number[1:4] == '495':
                print("YES")
            else:
                print('NO')
        else:
            print('NO')
else:
    for number in phone_book:
        if number[1:] in new_number[1:]:
            if number[1:] == new_number[1:]:
                print('YES')
            elif number == new_number[4:] and new_number[1:4] == '495':
                print("YES")
            else:
                print('NO')
        else:
            print('NO')