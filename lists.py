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

x = input().split()
for i in x:
    print(i)

x = input().split()
for i in x:
    print(i[0], end='.')

x = input().split('\\')
for i in x:
    print(i)

x = input().split()
for i in x:
    print('+' * int(i))

x = input().split('.')
flag = True
for i in x:
    if int(i) < 0 or int(i) > 255:
        flag = False
if flag == True:
    print('ДА')
else:
    print('НЕТ')

x = input()
y = input()
print(*x, sep=y)

x = input().split()
total = 0
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        if x[i] == x[j]:
            total +=1
print(total)

numbers = [8, 9, 10, 11]
numbers.pop(1)
numbers.insert(1, 17)
numbers.extend([4, 5, 6])
numbers.pop(0)
numbers = numbers * 2
numbers.insert(3, 25)
print(numbers)

x = input().split()
maxi = x.index(max(x, key=int))
mini = x.index(min(x, key=int))
x[maxi], x[mini] = x[mini], x[maxi]
print(*x)

x = input().lower().split()
total1 = x.count('an')
total2 = x.count('a')
total3 = x.count('the')
print('Общее количество артиклей:', total1 + total2 + total3)

a = input()
for i in range(int(a[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())

x = input().split()
for i in range(len(x)):
    x[i] = int(x[i])
x.sort()
print(*x)
x.sort(reverse=True)
print(*x)

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [keyword[1:] for keyword in keywords]
print(new_keywords)

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(keyword) for keyword in keywords]
print(lengths)

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [i for i in keywords if len(i) > 4]
print(new_keywords)

palindromes = [i for i in range(100, 1000) if str(i) == str(i)[::-1]]
print(palindromes)

x = [i ** 2 for i in range(1, int(input()) + 1)]
print(*x, sep='\n')

x = [int(i) ** 3 for i in input().split()]
print(*x)

print(*[i for i in input().split()], sep='\n')

print(*[i for i in input() if i in '0123456789'], sep='')

print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4])

a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
n = len(a)
a.sort()
print(a)

a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
n = len(a)
for i in range(n - 1):
    flag = True
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            flag = False
    if flag:
        break
print(a)