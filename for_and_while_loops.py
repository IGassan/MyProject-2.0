for i in range(10):
    print('Python is awesome!')

a = input()
b = int(input())
for i in range(b):
    print(a)

for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')

a = int(input())
for i in range(a):
    print('*' * 19)

a = input()
for i in range(10):
    print(i, a)

a = int(input())
for i in range(a + 1):
    print('Квадрат числа', i, 'равен', pow(i, 2))

a = int(input())
for i in range(a):
    print('*' * (a - i))

a = int(input())
b = int(input())
c = int(input())
f = a
for i in range(c):
    print(i + 1, f)
    f += f * (b / 100)

a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)

a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

a = int(input())
b = int(input())
for i in range(a, b - 1, -1):
    if i % 2 != 0:
        print(i)

a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
        print(i)

a = int(input())
for i in range(1, 11):
    print(a, 'x', i, '=', i * a)

total = 0
for i in range(1, 6):
    total += i
    print(total, end='')

a = int(input())
b = int(input())
total = 0
for i in range(a, b + 1):
    if pow(i, 3) % 10 == 4 or pow(i, 3) % 10 == 9:
        total += 1
print(total)

a = int(input())
total = 0
for i in range(a):
    x = int(input())
    total += x
print(total)

from math import *
a = int(input())
total = 0
if a == 1:
    total = 1.0
else:
    for i in range(2, a + 1):
        total += 1 / i
    total = (1 + total) - log(a)
print(total)

a = int(input())
total = 0
for i in range(a + 1):
    if pow(i, 2) % 10 == 2 or pow(i, 2) % 10 == 5 or pow(i, 2) % 10 == 8:
        total += i
print(total)

a = int(input())
total = 1
for i in range(1, a + 1):
    total *= i
print(total)

total = 1
for i in range(10):
    x = int(input())
    if x > 0:
        total *= x
print(total)

a = int(input())
total = 0
for i in range(1, a + 1):
    if a % i == 0:
        total += i
print(total)

a = int(input())
total = 0
for i in range(1, a + 1):
    if i % 2 == 0:
        total -= i
    else:
        total += i
print(total)

a = int(input())
total = 0
totol = 0
for i in range(a):
    x = int(input())
    if x > total:
        totol = total
        total = x
    elif x > totol:
        totol = x
print(total)
print(totol)

total = 0
for i in range(10):
    x = int(input())
    if x % 2 != 0:
        total += 1
if total == 0:
    print('YES')
else:
    print('NO')

a = int(input())
total = 1
totyl = 0
for i in range(1, a + 1):
    b = total
    total = b + totyl
    totyl = b
    print(b, end=' ')