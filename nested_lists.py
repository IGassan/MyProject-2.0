list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2, 7000)
print(list1)


list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].extend(sub_list)
print(list1)


list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1
for i in list1:
    if max(i) > maximum:
        maximum = max(i)
print(maximum)


list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
for i in list1:
    i.reverse()
print(list1)


list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for i in list1:
    counter += len(i)
    for j in i:
        total += j
print(total / counter)


a = int(input())
for i in range(a):
    lists = []
    for j in range(1, a + 1):
        lists.append(j)
    print(lists)


a = int(input())
for i in range(1,a + 1):
    lists = []
    for j in range(1, i + 1):
        lists.append(j)
    print(lists)


from enum import Flag
from math import *
from re import M

a = int(input())
lists = []
for i in range(a + 1):
    lists.append(int((factorial(a)) / (factorial(i) * factorial(a - i))))
print(lists)


def pascal(n):
    triangle = [[1]]
    
    for i in range(n):
        row = [1]
        for j in range(1, len(triangle[i])):
            row += [sum(triangle[i][j - 1: j + 1])]
        row += [1]
        triangle.append(row.copy())
        
    return triangle[n]

a = int(input())
for i in range(a):
    print(*pascal(i))


char_lists = []
a = []
for char in input().split():
    if a == []:
        a.append(char)
    else:
        if a[0] == char:
            a.append(char)
        else:
            char_lists.append(a)
            a = []
            a.append(char)
if a:
    char_lists.append(a)
print(char_lists)


a = input().split()
n = int(input())
total = list()
for i in range(0, len(a), n):
    total.append(a[i: i + n])
print(total)


input_data = input().split()
output_data = [[]]
for i in range(len(input_data)):
    for j in range(len(input_data) - i):
        output_data.append(input_data[j: j + i + 1])
print(output_data)

n = int(input())
m = int(input())
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for  j in range(m):
        matrix[i][j] = input()
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()


n = int(input())
m = int(input())
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for  j in range(m):
        matrix[i][j] = input()
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
print()
for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()


matrix = [input().split() for _ in range(int(input()))]
total = 0
for i in range(len(matrix)):
    for  j in range(len(matrix[i])):
        if i == j:
            total += int(matrix[i][j])
print(total)


matrix = [list(map(int, input().split())) for _ in range(int(input()))]
total = 0
for i in range(len(matrix)):
    for  j in range(len(matrix[i])):
        if matrix[i][j] > sum(matrix[i]) / len(matrix[i]):
            total += 1
    print(total)
    total = 0


matrix = [list(map(int, input().split())) for _ in range(int(input()))]
total = -10000
for i in range(len(matrix)):
    for  j in range(len(matrix[i])):
        if i >=j:
            if matrix[i][j] > total:
                total = matrix[i][j]
print(total)


matrix = [list(map(int, input().split())) for _ in range(int(input()))]
total = -1000
for i in range(len(matrix)):
    for  j in range(len(matrix[i])):
        if  (j <= i <= len(matrix) - 1 - j) or len(matrix) - 1 - j <= i <= j:
            if matrix[i][j] > total:
                total = matrix[i][j]
print(total)


matrix = [list(map(int, input().split())) for _ in range(int(input()))]
total1 = 0
total2 = 0
total3 = 0
total4 = 0
for i in range(len(matrix)):
    for  j in range(len(matrix[i])):
        if  i < j and i < len(matrix) - 1 - j:
            total1 += matrix[i][j]
        if  i < j and i > len(matrix) - 1 - j:
            total2 += matrix[i][j]
        if  i > j and i > len(matrix) - 1 - j:
            total3 += matrix[i][j]
        if  i > j and i < len(matrix) - 1 - j:
            total4 += matrix[i][j]
print('Верхняя четверть:', total1)
print('Правая четверть:', total2)
print('Нижняя четверть:', total3)
print('Левая четверть:', total4)


n = int(input())
m = int(input())
matrix = [[0] * m for _ in range(n)]
for i in range(len(matrix)):
    for  j in range(len(matrix[i])):
        matrix[i][j] = i * j
for i in range(len(matrix)):
    for  j in range(len(matrix[i])):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
total = max(max(matrix, key=max))
for i in range(len(matrix)):
    for  j in range(len(matrix[i])):
        if matrix[i][j] == total:
            print(i, j)
            break
    if matrix[i][j] == total:
        break


n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
total = input().split()
for i in range(len(matrix)):
    for  j in range(len(matrix[i])):
        if j == int(total[0]):
            matrix[i][j], matrix[i][int(total[1])] = matrix[i][int(total[1])], matrix[i][j]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()


n = int(input())
flag = True
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(len(matrix)):
    for  j in range(len(matrix[i])):
        if matrix[i][j] != matrix[j][i]:
            flag = False
if flag:
    print('YES')
else:
    print('NO')


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
total = [0] * n
for i in range(len(matrix)):
    h = matrix[i][i]
    matrix[i][i] = matrix[n - 1 - i][i]
    matrix[n - 1 - i][i] = h
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix.reverse()
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix.reverse()
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[j][i], end=' ')
    print()


xy = input()
a = '87654321'.index(xy[1])
b = 'abcdefgh'.index(xy[0])
matrix = [['.'] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        if i == int(a) and j == int(b):
            matrix[i][j] = 'N'
        if (int(b) - j) * (int(a) - i) == 2 or (int(b) - j) * (int(a) - i) == -2:
            matrix[i][j] = '*'
for i in range(8):
    for j in range(8):
        print(matrix[i][j], end=' ')
    print()


def magic_square():
    
    cols = int(input())
    matrix = []
    sum_main_diag = 0
    sum_semi_diag = 0
    check = []

    for i in range(cols):
        elem = [int(num) for num in input().split()]
        matrix.append(elem)

    for i in range(cols):
        check += matrix[i]

    for i in range(1, len(check) + 1):
        if i not in check:
            return print("NO")

    for i in range(cols):
        sum_main_diag += matrix[i][i]
        sum_semi_diag += matrix[i][cols - 1 - i]

    for i in range(cols):
        sum_cols = 0
        sum_rows = 0
        for j in range(cols):
            sum_cols += matrix[i][j]
            sum_rows += matrix[j][i]
        if not sum_cols == sum_rows == sum_main_diag == sum_semi_diag:
            return print("NO")
    else:
        return print("YES")

magic_square()


a = input().split()
n = int(a[0])
m = int(a[1])
matrix = [[0]* m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            matrix[i][j] = '.'
        else:
            matrix[i][j] = '*'
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()


n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == n - j - 1:
            matrix[i][j] = 1
        elif i > n - j - 1:
            matrix[i][j] = 2
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()



a = input().split()
n = int(a[0])
m = int(a[1])
total = 0
matrix = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        total += 1
        matrix[i][j] = total
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


a = input().split()
n = int(a[0])
m = int(a[1])
matrix = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = i + j * n + 1
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == n - j - 1 or i == j:
            matrix[i][j] = 1
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()


n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if (i <= j and i <= n - 1 - j) or (i >= j and i >= n - 1 - j):
            matrix[i][j] = 1
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()


a = input().split()
n = int(a[0])
m = int(a[1])
matrix = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()


a = input().split()
n = int(a[0])
m = int(a[1])
total = 0
matrix = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        total += 1
        matrix[i][j] = total
for i in range(n):
    if i % 2 != 0:
        matrix[i].reverse()
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


a = input().split()
n = int(a[0])
m = int(a[1])
total = 0
matrix = [[0] * m for i in range(n)]
for j in range(m + n - 1):
    for i in range(n):
        if j - i in range(m):
            total += 1
            matrix[i][j - i] = total
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]
dr, dc, r, c = 0, 1, 0, 0

for cnt in range(1, n * m + 1):
    a[r][c] = cnt
    
    if a[(r + dr) % n][(c + dc) % m]:
        dr, dc = dc, -dr

    r += dr
    c += dc    
    
for row in a:
    print(*(f'{e:<3}' for e in row), sep='')


a = input().split()
n = int(a[0])
m = int(a[1])
matrix1 = [list(map(int, input().split())) for _ in range(n)]
box = input()
matrix2 = [list(map(int, input().split())) for _ in range(n)]
matrix3 = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
for i in range(n):
    for j in range(m):
        print(matrix3[i][j], end=' ')
    print()


n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrixB = [[int(i) for i in input().split()] for _ in range(m)]
matrixC = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for q in range(m):
            matrixC[i][j] += matrixA[i][q] * matrixB[q][j]

for row in matrixC:
    print(*row)


n = int(input())
m1 = [[int(j) for j in input().split()] for i in range(n)]
m = int(input())
res = m1

for l in range(m-1):
    res = [[sum([res[i][p] * m1[p][j] for p in range(n)]) for j in range(n)] for i in range(n)]

for r in res:
    print(*r)