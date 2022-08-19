a = input()
b = input()
if a == b:
    print('Пароль принят')
else:
    print('Пароль не принят')

a = int(input())
if a % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

z = int(input())
a = z // 1000
b = z % 1000 // 100
c = z % 100 // 10
d = z % 10
if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')

z = int(input())
if z > 17:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

a = int(input())
b = int(input())
c = int(input())
if c == (b - a) + b:
    print('YES')
else:
    print('NO')

a, b = int(input()), int(input())
if a > b:
    print(b)
else:
    print(a)

a, b, c, d = int(input()), int(input()), int(input()), int(input())
ab, cd = 0, 0
if a > b:
    ab = b
else:
    ab = a
if c > d:
    cd = d
else:
    cd = c
if ab > cd:
    print(cd)
else:
    print(ab)

a = int(input())
if a < 14:
    print('детство')
if 13 < a < 25:
    print('молодость')
if 24 < a < 60:
    print('зрелость')
if 59 < a:
    print('старость')

a, b, c = int(input()), int(input()), int(input())
counter = 0
if a > 0:
    counter += a
if b > 0:
    counter += b
if c > 0:
    counter += c
print(counter)

a = int(input())
if -1 < a < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

a = int(input())
if a <= -3 or a >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

a = int(input())
if -30 < a <= -2 or 7 < a <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

a = int(input())
if 999 < a < 10000 and (a  % 7 == 0 or a % 17 == 0):
    print('YES')
else:
    print('NO')

a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and c + b > a:
    print('YES')
else:
    print('NO')

a = int(input())
if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
    print('YES')
else:
    print('NO')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a == c) or (b == d):
    print('YES')
else:
    print('NO')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a - c == 1 or c - a == 1 or a == c) and (b - d == 1 or d - b == 1 or b == d):
    print('YES')
else:
    print('NO')

a, b = int(input()), int(input())
if a < b:
    print('YES')
elif a > b:
    print('NO')
else:
    print("Don't know")

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b or b == c or a == c:
    print('Равнобедренный')
else:
    print('Разносторонний')

a, b, c = int(input()), int(input()), int(input())
if a > b > c or a < b < c:
    print(b)
elif a > c > b or a < c < b:
    print(c)
else:
    print(a)

a = int(input())
if a == 2:
    print(28)
elif a == 4 or a ==  6 or a == 9 or a == 11:
    print(30)
else:
    print(31)

a = int(input())
if a < 60:
    print('Легкий вес')
elif a < 64:
    print('Первый полусредний вес')
else:
    print('Полусредний вес')

a, b, c = int(input()), int(input()), input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')

a, b = input(), input()
if a == 'красный':
    if b == 'красный':
        print('красный')
    elif b == 'синий':
        print('фиолетовый')
    elif b == 'желтый':
        print('оранжевый')
    else:
        print('ошибка цвета')
elif a == 'синий':
    if b == 'синий':
        print('синий')
    elif b == 'желтый':
        print('зеленый')
    elif b == 'красный':
        print('фиолетовый')
    else:
        print('ошибка цвета')
elif a == 'желтый':
    if b == 'желтый':
        print('желтый')
    elif b == 'красный':
        print('оранжевый')
    elif b == 'синий':
        print('зеленый')
    else:
        print('ошибка цвета')
else:
    print('ошибка цвета')

a = int(input())
if a == 0:
    print('зеленый')
elif 1 <= a <= 10 or 19 <= a <= 28:
    if a % 2 == 0:
        print('черный')
    else:
        print('красный ')
elif 11 <= a <= 18 or 29 <= a <= 36:
    if a % 2 == 0:
        print('красный')
    else:
        print('черный ')
else:
    print('ошибка ввода')

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a1 < b1 < a2 or a2 < b2 < a1:
    print('пустое множество')
elif  a1 <= a2 and b1 >= b2:
    print(a2, b2)
elif a2 <= a1 and b2 >= b1:
    print(a1, b1)
elif b2 == a1:
    print(b2)
elif b1 == a2:
    print(b1)
elif a1 < a2 < b1 < b2:
    print(a2, b1)
elif a2 < a1 < b2 < b1:
    print(a1, b2)
else:
    print('пустое множество')

# Итоговая работа

a = int(input())
if a % 10 == 0 and (a % 100) // 10 == 0:
    print('YES')
else:
    print('NO')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a + b + c + d) % 2 == 0:
    print('YES')
else:
    print('NO')

a, b = int(input()), input()
if 10 <= a <= 15 and b == 'f':
    print('YES')
else:
    print('NO')

a = int(input())
if a < 1 or a > 10:
    print('ошибка')
elif a == 1:
    print('I')
elif a == 2:
    print('II')
elif a == 3:
    print('III')
elif a == 4:
    print('IV')
elif a == 5:
    print('V')
elif a == 6:
    print('VI')
elif a == 7:
    print('VII')
elif a == 8:
    print('VIII')
elif a == 9:
    print('IX')
elif a == 10:
    print('X')

a = int(input())
if a % 2 != 0 or (6 <= a <= 20 and a % 2 == 0):
    print('YES')
else:
    print('NO')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a + b == c + d) or (a == b and c == d) or (a - b == c - d):
    print('YES')
else:
    print('NO')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if abs(a - c) == abs(b - d):
    print('YES')
else:
    print('NO')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if abs(a - c) == abs(b - d) or (a == c) or (b == d):
    print('YES')
else:
    print('NO')