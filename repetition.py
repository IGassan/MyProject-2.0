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