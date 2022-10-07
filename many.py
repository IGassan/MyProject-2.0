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