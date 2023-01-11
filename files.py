n = input()
file = open(n)
print(*n)
file.close()


n = input()
file = open(n)
line = file.readlines()[-2]
print(line)
file.close()

import random

file = open('lines.txt', encoding='utf-8')
line = file.readlines()[random.randrange(list(line))]
print(line)
file.close()


file = open('numbers.txt', encoding='utf-8')
print(sum(map(int, file)))
file.close()


file = open('nums.txt', encoding='utf-8')
print(sum([int(i) for i in file.read().split()]))
file.close()


file = open('prices.txt')
lines = map(str.split, file)
print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
file.close()


with open('text.txt', encoding='utf-8') as file:
    line = file.read()
    print(line[::-1])


with open('data.txt', encoding='utf-8') as file:
    lines = file.readlines()[::-1]
    for line in lines:
        print(line, end='')


with open('lines.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    longest = max(map(len, lines))
    print(*filter(lambda x: len(x) == longest, lines), sep='\n')


with open('numbers.txt') as f:
    for line in f:
        print(sum(map(int, line.split())))


with open('nums.txt') as f:
    num = ''
    lst = []
    for s in f.read():
        if s.isdigit():
            num += s
        else:
            if num:
                lst.append(int(num))
                num = ''
    print(sum(lst))


with open('lines.txt') as f:
    txt = f.read()
    print('Input file contains:')
    print(sum(map(str.isalpha, txt)), 'letters')
    print(len(txt.split()), 'words')
    print(txt.count('\n') + 1, 'lines')


import random
with open('first_names.txt') as names, open('last_names.txt') as surnames:
    name = names.read().split()
    surname = surnames.read().split()
    print(f'{name[random.randint(1, len(name))]} {surname[random.randint(1, len(surname))]}')
    print(f'{name[random.randint(1, len(name))]} {surname[random.randint(1, len(surname))]}')
    print(f'{name[random.randint(1, len(name))]} {surname[random.randint(1, len(surname))]}')