""" for i in range(10):
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
from sys import flags
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

a = input()
while a != 'КОНЕЦ':
    print(a)
    a = input()

a = input()
while a != 'КОНЕЦ' and a != 'конец':
    print(a)
    a = input()

a = input()
total = 0
while a != 'стоп' and a != 'хватит' and a != 'достаточно':
    total += 1
    a = input()
print(total)

a = int(input())
while a  % 7 == 0:
    print(a)
    a = int(input())

a = int(input())
total = 0
while 0 <= a < 6:
    if a == 5:
        total += 1
    a = int(input())
print(total)

a = int(input())
total = 0
while 0 < a:
    if a >= 25:
        a -= 25
        total += 1
    elif a >= 10:
        a -= 10
        total += 1
    elif a >= 5:
        a -= 5
        total += 1
    else:
        a -= 1
        total += 1
print(total)

a = int(input())
while a != 0:
    last_number = a % 10
    print(last_number)
    a = a // 10

a = int(input())
while a != 0:
    last_number = a % 10
    print(last_number, end='')
    a = a // 10

a = int(input())
max = 0
min = 9
while a != 0:
    last_number = a % 10
    if max < last_number:
        max = last_number
    if min > last_number:
        min = last_number
    a //= 10
print('Максимальная цифра равна', max)
print('Минимальная цифра равна', min)

a = int(input())
sum = 0
kol = 0
proiz = 1
sumfl = a % 10
while a != 0:
    last_number = a % 10
    sum += last_number
    kol += 1
    proiz *= last_number
    a //= 10
print(sum)
print(kol)
print(proiz)
print(sum / kol)
print(last_number)
print(last_number + sumfl)

a = input()
print(a[1])

a = int(input())
max = 0
min = 9
while a != 0:
    last_number = a % 10
    if max < last_number:
        max = last_number
    if min > last_number:
        min = last_number
    a //= 10
if max == min:
    print('YES')
else:
    print('NO')

a = int(input())
b = a // 10
flags = 'YES'
while a > 10:
    alast_number = a % 10
    blast_number = b % 10
    if alast_number > blast_number:
        flags = 'NO'
    a = a // 10
    b = b // 10
print(flags)

a = int(input())
b = 2
while b <= a :
    if a % b == 0:
        print(b)
        break
    b += 1

a = int(input())
for i in range(1, a + 1):
    if 4 < i < 10:
        continue
    elif 16 < i < 38:
        continue
    elif 77 < i < 88:
        continue
    else:
        print(i)

from math import *
count = 0
p = 1
for i in range(10):
    x = int(input())
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')

mx = -10 ** 6
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        if x > mx:
            mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')

s = 0
for i in range(7):
    n = int(input())
    if n % 2 == 0:
        s += n
print(s)

n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)

n = int(input())
while n > 9:
    n //= 10
print(n)

n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)

x = int(input())
for i in range(x):
    for j in range(3):
        print(x, end=' ')
    print()

x = int(input())
for i in range(1, x + 1):
    for j in range(5):
        print(i, end=' ')
    print()

x = int(input())
for i in range(1, x + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()

x = int(input())
for i in range(x // 2 + 1):
    for j in range(i + 1):
        print('*', end='')
    print()
for i in range(x // 2 - 1, -1, -1):
    for j in range(i + 1):
        print('*', end='')
    print()

x = int(input())
for i in range(1, x + 1):
    for j in range(i):
        print(i, end='')
    print()

for i in range(1, 15):
    for j in range(1, 15):
        for k in range(1, 15):
            if 28 * i + 30 * j + 31 * k == 365:
                print('n', i, 'k', j, 'm', k)

for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            if i + j + k == 100 and 10 * i + 5 * j + 0.5 * k == 100:
                print(i, j , k)

x = int(input())
total = 0
for i in range(1, x + 1):
    for j in range(i):
        total += 1
        print(total, end=' ')
    print()

x = int(input())
for i in range(1, x + 1):
    for j in range(i):
        print(j + 1, end='')
    for k in range(i -1, 0, -1):
        print(k, end='')
    print()

x = int(input())
y = int(input())
total = 0
max_total = 0
numb_total = 0
for i in range(x, y + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
    if total >= max_total:
        max_total = total
        numb_total = i
    total = 0
print(numb_total, max_total)

x = int(input())
total = 0
for i in range(1, x + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            total += 1
    print(i, '+' * total, sep='')
    total = 0

x = int(input())
total = 0
totol = 0
while x > 0:
    total += x % 10
    x //= 10
while total > 0:
    totol += total % 10
    total //= 10
if totol > 9:
    print(totol // 10 + totol % 10 )
else:
    print(totol)

x = int(input())
total = 0
for i in range(1, x + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            total += 1
    print(i, '+' * total, sep='')
    total = 0

from math import *
x = int(input())
total = 0
for i in range(1, x + 1):
    total += factorial(i)
print(total) """

x = int(input())
y = int(input())
total = 0
for i in range(x, y + 1):
    for j in (1, i + 1):
        if i % j == 0:
            total += 1
    if total == 2:
        print(i)
    total = 0