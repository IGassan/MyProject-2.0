import random

n = int(input())
for _ in range(n):
    tot = random.randint(0,1)
    if tot == 1:
        print('Орел')
    else:
        print('Решка')


import random

n = int(input()) 
for _ in range(n):
    print(random.randint(1, 6))


import random

length = int(input()) 
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(length):
    print(chars[random.randint(1, 51)], end='')


import random

n = set()
for _ in range(7):
    n.add(random.randint(1, 49))
print(*sorted(n))


import random

def generate_ip():
    return '.'.join([str(random.choice(range(256))) for _ in range(4)])


import random, string

def generate_index():
    st1 = ''.join([random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase)])
    st2 = ''.join([random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase)])
    st3 = '_'.join([str(random.choice(range(100))), str(random.choice(range(100)))])
    return st1 + st3 + st2


import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
random.shuffle(matrix)


import random

for i in range(100):
    print(random.randint(1000000, 9999999))


import random

n = input()
print(*random.sample(n, len(n)), sep='')


import random

matrix = random.sample(list(range(1, 76)), 25)
tot = 0
matrix[12] = 0
for i in range(5):
    for j in range(5):
        print(str(matrix[tot]).ljust(3), end=' ')
        tot +=1
    print()


from random import choice

names, rel, tmp = {input() for _ in range(int(input()))}, {}, 0
for name in names.copy():
    if names == {name}:
        rel[tmp], rel[name] = name, rel[tmp]
    else:
        rand_name = choice(list(names - {name}))
        rel[name] = rand_name
        names -= {rand_name}
        tmp = name
[print(k, '-', v) for k, v in rel.items()]


from string import *
from random import sample

def generate_password(length):
    LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
    return ''.join(sample(LETTER, length))

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')


import string, random

def generate_password(length):
    symbols = ([x for x in string.ascii_uppercase if x not in 'OI'],
               [x for x in string.ascii_lowercase if x not in 'ol'],
               [x for x in string.digits[2:]])
    
    password = [random.choice(symbols[i]) for i in range(3)]
    password += random.sample(''.join([''.join(symbols[i]) for i in range(3)]), length - 3)
    random.shuffle(password)
    return ''.join(password)
    
def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')


import random

n = 10**6 
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if x**3 + y**4 + 2 >= 0 and 3 * x + y**2 <= 2:
        k += 1
print((k / n) * s0)


import random

n = 10**6 
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if x**2 + y**2 <= 1:
        k += 1
print((k / n) * s0)