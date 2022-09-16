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


from math import *

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