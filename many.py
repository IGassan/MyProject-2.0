n = int(input())
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())
total = z + m + n - x + k - y
print(total)


n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))
i = n + m + k
j = x + y + z
print(3 * (t - i) + 2 * j)
print(2 * i - j - 3 * t)
print(a + i - j - t)


numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
total = min(numbers) + max(numbers)
print(total)


numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
average = sum(numbers) / len(numbers)
print(average)


numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
total = 0
for num in numbers:
    total += num ** 2
print(total)


fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
total = sorted(fruits, reverse=True)
print(*total, sep='\n')


n = set(input())
print(len(n))


n = input()
total = set(n)
if len(n) == len(total):
    print('YES')
else:
    print('NO')


n = set(input() + input())
if len(n) > 9:
    print('YES')
else:
    print('NO')

n = set(input())
m = set(input())
if n == m:
    print('YES')
else:
    print('NO')


n = input().split()
n1 = set(n[0])
n2 = set(n[1])
n3 = set(n[2])
if n1 == n2 == n3:
    print('YES')
else:
    print('NO')


n = int(input())
for i in range(n):
    print(len(set(input().lower())))


n = int(input())
total = set()
for i in range(n):
    total.update(input().lower())
print(len(total))


print(len(set(x.strip('.,;:-?!') for x in input().lower().split())))


total = list(input().split())
for i in range(len(total)):
    total[i] = int(total[i])
tot = set()
for i in total:
    if i not in tot:
        tot.add(i)
        print('NO')
    elif i in tot:
        print('YES')

    
a, b = set(input().split()), set(input().split())
print(len(a.intersection(b)))


a, b = set(int(i) for i in input().split()), set(int(i) for i in input().split())
c = sorted(a.intersection(b))
print(*c)


a, b = set(int(i) for i in input().split()), set(int(i) for i in input().split())
c = sorted(a.difference(b))
print(*c)


n = int(input())
a1 = set(input().split())
for i in range(n - 1):
    a1.intersection_update(input())
print(a1)


n = int(input())
a1 = set(input())
for i in range(n - 1):
    a1.intersection_update(set(input()))
print(*sorted(a1))


a = set(input())
b = set(input())
if a.isdisjoint(b):
    print('NO')
else:
    print('YES')


set1, set2 = set(input()), set(input()) 
print('YES' if set2.issubset(set1) else 'NO')


set1, set2, set3 = set(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))
total = set1 & set2
total = total - set3
print(*sorted(total, reverse=True))


set1, set2, set3 = set(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))
total = set1.intersection(set2, set3)
totol = set1.union(set2, set3)
print(*sorted(totol.difference(total)))


set1, set2, set3 = set(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))
total = set1.union(set2)
totol = set3.difference(total)
print(*sorted(totol, reverse=True))


set1, set2, set3 = set(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))
total = set1.union(set2, set3)
totol = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(*sorted(totol.difference(total)))


items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
myset = {int(i) for i in items}
print(*sorted(myset))


words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
myset = {i[0].lower() for i in words}
print(*sorted(myset))


sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
for i in sentence:
    if i in ".,;:-?!()":
        sentence=sentence.replace(i,"")
myset = {i.lower() for i in sentence.split()}
print(*sorted(myset))


sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
for i in sentence:
    if i in ".,;:-?!()":
        sentence=sentence.replace(i,"")
myset = {i.lower() for i in sentence.split() if len(i) < 4}
print(*sorted(myset))


files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
myset = {i.lower() for i in files if i[-4:].lower() == '.png'}
print(*sorted(myset))


set1 = {'a', 't', 'f', 'p'}
set2 = {'a', 't', 'f'}
print(set1 - set2)


n, m, k, p = int(input()), int(input()), int(input()), int(input())
print(n - m - k + p)

n = input().split()
total = set(n)
print(len(n) - len(total))


n = int(input())
total = {input() for _ in range(n)}
m = input()
if m in total:
    print('REPEAT')
else:
    print('OK')


m = int(input())
n = int(input())
totalm = {input() for _ in range(m)}
totaln = (input() for _ in range(n))
for i in totaln:
    if i in totalm:
        print('YES')
    else:
        print('NO')


m = set(input().split())
n = set(input().split())
total = n.intersection(m)
if len(total) > 0:
    print(*sorted(total, reverse=True, key=int))
else:
    print('BAD DAY')


m = {int(i) for i in input().split()}
n = {int(i) for i in input().split()}
if n == m:
    print('YES')
else:
    print('NO')


m = int(input())
n = int(input())
totalm = {input() for _ in range(m)}
totaln = {input() for _ in range(n)}
total = totalm - totaln
print(len(total))


m = int(input())
n = int(input())
totalm = {input() for _ in range(m)}
totaln = {input() for _ in range(n)}
total = totalm ^ totaln
if len(total) > 0:
    print(len(total))
else:
    print('NO')


m = set(input().split())
n = set(input().split())
total = m.union(n)
print(*sorted(total))


m, n = int(input()), int(input())
set1 = set()
set2 = set()
for i in range(m + n):
    a = input()
    if a in set1:
        set2.add(a)
    else:
        set1.add(a)
print(len(set1 ^ set2) if len(set1 ^ set2) > 0 else "NO")


m = int(input())
set1 = set()
for i in range(m):
    n = int(input())
    set2 = set()
    if i == 0:
        for j in range(n):
            set1.add(input())
    else:
        for j in range(n):
            set2.add(input())
            
        set1.intersection_update(set2)
        
print(*sorted(set1), sep='\n')