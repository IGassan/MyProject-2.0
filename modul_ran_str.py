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