a = float(input())
b = float(input())
print(0.5 * a * b)

a = float(input())
b = float(input())
c = float(input())
print(a / (c + b))

a = float(input())
if a == 0:
    print('Обратного числа не существует')
else:
    print(1 / a)

a = float(input())
print(5 / 9 * (a - 32))

a = int(input())
if a == 1:
    print(10.5)
elif a == 2:
    print(21)
else:
    print(21 + (a - 2) * 4)

a = float(input())
number = (a * 10) % 10
print(int(number)) 

a = float(input())
print(a % 1)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print('Наименьшее число =', min(a, b, c, d, e))
print('Наибольшее число =', max(a, b, c, d, e))

a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))
print((a + b + c) - max(a, b, c) - min(a, b, c))
print(min(a, b, c))

a = int(input())
a1 = a // 100
a2 = (a % 100) // 10
a3 = a % 10
if (max(a1, a2, a3) - min(a1, a2, a3)) == (a1 + a2 + a3 - max(a1, a2, a3) - min(a1, a2, a3)):
    print('Число интересное')
else:
    print('Число неинтересное')

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
print(abs(a) + abs(b) + abs(c)+ abs(d) + abs(e))

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(abs(a - c) + abs(b - d))

print('"Python is a great language!", said Fred. "I' + " don't ever" + ' remember having this much fun before."')

a = input()
b = input()
print('Hello ' + a + ' ' + b + '! You just delved into Python')

a = input()
print('Футбольная команда ' + a + ' имеет длину ' + str(len(a)) + ' символов')

a = input()
b = input()
c = input()
if len(a) < len(b) and len(a) < len(c):
    print(a)
elif len(b) < len(a) and len(b) < len(c):
    print(b)
else:
    print(c)
if len(a) > len(b) and len(a) > len(c):
    print(a)
elif len(b) > len(a) and len(b) > len(c):
    print(b)
else:
    print(c)

a = input()
b = input()
c = input()
if (2 * len(b) - len(c) - len(a)) * (2 * len(c) - len(b) - len(a)) * (2 * len(a) - len(b) - len(c)) == 0:
    print('YES')
else:
    print('NO')

a = input()
if 'синий' in a:
    print('YES')
else:
    print('NO')

a = input()
if 'суббота' in a or 'воскресенье' in a:
    print('YES')
else:
    print('NO')

a = input()
if '.' in a and '@' in a:
    print('YES')
else:
    print('NO')

from math import *
a = sqrt(2)

from math import *
a = float(input())
b = float(input())
c = float(input())
d = float(input())
print(sqrt(pow(a - c, 2) + pow(b - d, 2)))

from math import *
a = float(input())
print(pi * pow(a, 2))
print(2 * pi * a)

from math import *
a = float(input())
b = float(input())
print((a + b) / 2)
print(sqrt(a * b))
print((2 * a * b) / (a + b))
print(sqrt((pow(a, 2) + pow(b, 2)) / 2))

from math import *
a = radians(float(input()))
print(sin(a) + cos(a) + pow(tan(a), 2))

from math import *
a = float(input())
print(ceil(a) + floor(a))

from math import *
a = float(input())
b = float(input())
c = float(input())
D = pow(b, 2) - 4 * a * c
if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    if  x1 > x2:
        print(x2, x1, sep='\n')
    else:
        print(x1, x2, sep='\n')
elif D == 0:
    print(-b / (2 * a))
else:
    print('Нет корней')

from math import *
n = int(input())
a = float(input())
print((n * pow(a, 2)) / (4 * tan(pi / n)))