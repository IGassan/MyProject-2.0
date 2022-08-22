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