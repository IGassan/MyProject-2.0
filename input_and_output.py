print("Здравствуй, мир!")

print(4, 8, 15, 16, 23, 42)

print(4)
print(8)
print(15)
print(16)
print(23)
print(42)

for i in range(1,8):
    print("*" * i)

name = input()
print('Привет,', name)

name = input()
print(name, '- чемпион!')

x = input()
y = input()
z = input()
print(x)
print(y)
print(z)

x = input()
y = input()
z = input()
print(z)
print(y)
print(x)

print('I', 'like', 'Python', sep='***')

a = input()
x = input()
y = input()
z = input()
print(x, y, z, sep=a)

name = input()
print('Привет,', name, end='')
print('!')

a = int(input())
print(a, a + 1, a + 2, sep='\n')

x = int(input())
y = int(input())
z = int(input())
print(z + y + x)

x = int(input())
print('Объем =', x ** 3)
print('Площадь полной поверхности =', 6 * x ** 2)

x = int(input())
y = int(input())
print(3 * (x + y) ** 3 + 275 * y ** 2 - 127 * x - 41)

x = int(input())
print('Следующее за числом', x, 'число:', x + 1)
print('Для числа', x, 'предыдущее число:', x - 1)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(3 * (a + b + c + d))

a = int(input())
b = int(input())
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)

a = int(input())
b = int(input())
c = int(input())
print(a + b * (c - 1))

a = int(input())
print(a, 2 * a, 3 * a, 4 * a, 5 * a, sep='---')

a = int(input())
b = int(input())
c = int(input())
print(a * b ** (c - 1))

a = int(input())
print(a // 100)

a = int(input())
b = int(input())
print(b // a)
print(b % a)

a = int(input())
print((a + 1) // 2)

a = int(input())
print((a + 3) // 4)

a = int(input())
print(a, 'мин - это', a // 60, 'час', a % 60, 'минут.')

a = int(input())
x = a // 100
y = (a % 100) // 10
z = a % 10
sum = x + y + z
proiz = x * y * z
print('Сумма цифр =', sum)
print('Произведение цифр =', proiz)

a = int(input())
x = str(a // 100)
y = str((a % 100) // 10)
z = str(a % 10)
print(x + y + z)
print(x + z + y)
print(y + x + z)
print(y + z + x)
print(z + x + y)
print(z + y + x)

x = int(input())
a = x // 1000
b = (x % 1000) // 100
c = (x % 100) // 10
d = x % 10
print('Цифра в позиции тысяч равна', a)
print('Цифра в позиции сотен равна', b)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', d)

# Итоговая работа

print('*' * 17)
print('*', ' ' * 13, '*')
print('*', ' ' * 13, '*')
print('*' * 17)

a = int(input())
b = int(input())
print('Квадрат суммы', a, 'и', b, 'равен', (a + b) ** 2)
print('Сумма квадратов', a, 'и', b, 'равна', a ** 2 + b ** 2)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a ** b + c ** d)

a = input()
print(int(a) + int(a * 2) + int(a * 3))