from math import sqrt
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(sqrt(a ** 10 + b ** 10))

a = float(input())
b = float(input())
if 18.5 <= (a / (b ** 2)) <= 25:
    print('Оптимальная масса')
elif(a / (b ** 2)) > 25:
    print('Избыточная масса')
else:
    print('Недостаточная масса')

a = input()
total = len(a) * 60
print(total // 100,'р.',total % 100,'коп.')

a = input().split()
print(len(a))

a = int(input())
animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
print(animals[a % 12])

a = input()
if len(a) == 5:
    print(int(a[::-1]))
else:
    print(int(a[0] + a[:-6:-1]))

a = list(input())
if len(a) > 3:
    a = a[::-1]
    add = 0
    for i in range(3, len(a), 3):
        a.insert(i + add, ',')
        add += 1
    a = a[::-1]
    print(*a, sep='')
else:
    print(*a, sep='')

n = int(input())
k = int(input())
total = 0
for i in range(1, n + 1):
    total = (total + k) % i
print(total + 1)

a = int(input())
total_1 = 0
total_2 = 0
total_3 = 0
total_4 = 0
for i in range(a):
    b = input().split()
    x = int(b[0])
    y = int(b[1])
    if x > 0 and y > 0:
        total_1 += 1
    elif x < 0 and y > 0:
        total_2 += 1
    elif x < 0 and y < 0:
        total_3 += 1
    elif x > 0 and y < 0:
        total_4 += 1
print('Первая четверть:', total_1)
print('Вторая четверть:', total_2)
print('Третья четверть:', total_3)
print('Четвертая четверть:', total_4)

a = input().split()
total = 0
for i in range(len(a) - 1):
    if int(a[i]) < int(a[i + 1]):
        total += 1
print(total)

a = input().split()
for i in range(0, len(a) - 1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
print(*a)

a = input().split()
total = a[len(a) - 1]
a.pop(len(a) - 1)
a.insert(0, total)
print(*a)

a = input().split()
total = 0
for i in range(len(a) - 1):
    if int(a[i]) != int(a[i + 1]):
        total += 1
print(total + 1)

a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
c = int(input())
flag = 'НЕТ'
for i in range(len(b)):
    for j in range(len(b)):
        if i != j:
            if b[i] * b[j] == c:
                flag = 'ДА'
print(flag)

a = input()
b = input()
if a == 'камень' and b == 'ножницы':
    print('Тимур')
elif a == 'ножницы' and b == 'бумага':
    print('Тимур')
elif a == 'бумага' and b == 'камень':
    print('Тимур')
elif a == b:
    print('ничья')
else:
    print('Руслан')

a = input()
b = input()
if a == 'камень' and (b == 'ножницы' or b == 'ящерица'):
    print('Тимур')
elif a == 'ножницы' and (b == 'бумага' or b == 'ящерица'):
    print('Тимур')
elif a == 'бумага' and (b == 'камень'or b == 'Спок'):
    print('Тимур')
elif a == 'ящерица' and (b == 'бумага'or b == 'Спок'):
    print('Тимур')
elif a == 'Спок' and (b == 'ножницы'or b == 'камень'):
    print('Тимур')
elif a == b:
    print('ничья')
else:
    print('Руслан')

a = input().split('О')
total = 0
for i in range(len(a)):
    if len(a[i]) > total:
        total = len(a[i])
print(total)

for i in range(int(input())):
    s, virus, x  = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break    

word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]
for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()