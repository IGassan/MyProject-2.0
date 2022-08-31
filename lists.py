x = list(range(1, int(input()) + 1))
print(x)

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x = int(input())
print(abc[:x])

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[16])

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[-1])

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[:6])

numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
print(max(numbers) + min(numbers))

evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)
print(average)

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3] = 'Зеленый'
rainbow[-1] = 'Фиолетовый'
print(rainbow)

languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])

numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]
print(numbers1 * 2 + numbers2 * 9 + numbers3)

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)

x = int(input())
z = list()
for i in range(x):
    x = input()
    z.append(x)
print(z)

abc = 'abcdefghijklmnopqrstuvwxyz'
z = list()
a = 1
for i in abc:
    z.append(i * a)
    a += 1
print(z)

x = int(input())
z = list()
for i in range(x):
    y = int(input())
    z.append(y ** 3)
print(z)

x = int(input())
z = list()
for i in range(1, x + 1):
    if x % i == 0:
        z.append(i)
print(z)

x = int(input())
z = list()
w = list()
for i in range(x):
    y = int(input())
    z.append(y)
for i in range(1, x):
    w.append(int(z[i]) + int(z[i - 1]))
print(w)

x = int(input())
z = list()
for i in range(x):
    y = int(input())
    if i % 2 == 1:
        continue
    z.append(y)
print(z)

x = int(input())
z = list()
for i in range(x):
    y = input()
    z.append(y)
w = int(input())
for i in range(x):
    if w > len(z[i]):
        continue
    print(z[i][w - 1], end='')

x = int(input())
z = list()
for i in range(x):
    y = input()
    z.extend(y)
print(z)

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
total = 0
for i in numbers:
    total += i ** 2
print(total)

x = int(input())
z = list()
for i in range(x):
    y = int(input())
    z.append(y)
print(*z, sep='\n')
print()
for i in z:
    i = i ** 2 + 2 * i + 1
    print(i)

x = int(input())
z = list()
for i in range(x):
    y = int(input())
    z.append(y)
for i in z:
    if i == max(z) or i == min(z):
        continue
    print(i)

x = int(input())
z = list()
for i in range(x):
    y = input()
    if y not in z:
        z.append(y)
print(*z, sep='\n')

x = int(input())
z = list()
for i in range(x):
    y = input()
    z.append(y)
w = input()
for i in z:
    if w.lower() in i.lower():
        print(i)

x = int(input())
z = list()
for i in range(x):
    y = input()
    z.append(y)
a = int(input())
c = list()
for i in range(a):
    b = input()
    c.append(b)
for i in z:
    flag = True
    for j in c:
        if j.lower() not in i.lower():
            flag = False
    if flag == True:
        print(i)

x = int(input())
z = list()
c = list()
for i in range(x):
    y = input()
    z.append(y)
for i in z:
    if int(i) < 0:
        c.append(i)
for i in z:
    if int(i) == 0:
        c.append(i)
for i in z:
    if int(i) > 0:
        c.append(i)
print(*c, sep='\n')