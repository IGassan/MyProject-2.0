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