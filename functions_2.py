def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    return [[value for _ in range(m)] for _ in range(n)]


def count_args(*args):
    return len(args)


def sq_sum(*args):
    sum = 0
    for i in args:
        sum += i**2
    return sum


def mean(*args):
    su = 0
    le = 0
    for i in args:
        if type(i) is float or type(i) is int:
            su += i
            le += 1
    if le == 0:
        return 0
    else:
        return su / le


def greet(name, *args):
    a = ' and '.join(args)
    if len(a) > 1:
        return 'Hello, ' + name + ' and ' + a + '!'
    else:
        return 'Hello, ' + name + '!'


def print_products(*args):
    a = 0
    for i in args:
        if type(i) is str and len(i) > 1:
            a += 1
            print(f'{a}) {i}')
    if a == 0:
        print('Нет продуктов')


def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
        print(f'{key}: {value}')


def total(number):
    return sum(number) / len(number)
numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
print(min(numbers, key=total))
print(max(numbers, key=total))


def total(number):
    return (number[0]**2 + number[1]**2)**0.5
    
points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
points.sort(key=total)
print(points)


def total(number):
    return min(number) + max(number)

numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
numbers.sort(key=total)
print(numbers)


def total(numb):
    return numb[answer - 1]

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
answer = int(input())
athletes.sort(key=total)
for i in athletes:
    print(*i)


from math import sin

def kvad(n):
    return n**2

def cub(n):
    return n**3

def sq(n):
    return n**0.5

def modu(n):
    return abs(n)

def sinu(n):
    return sin(n)

n = int(input())
mod = input()
func = {'квадрат': kvad, 'куб': cub, 'корень': sq, 'модуль': modu, 'синус': sinu}
func[mod](n)


n = input().split()

def func(number):
    sum = 0
    number = int(number)
    while number > 0:
        sum += number % 10
        number //= 10
    
    return sum

print(sorted(n, key=func))


n = input().split()

def funct(number):
    number = int(number)
    return number

def func(number):
    sum = 0
    number = int(number)
    while number > 0:
        sum += number % 10
        number //= 10
    
    return sum

n.sort(key=funct)
n.sort(key=func)
print(*n)


def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def krug(x):
    return round(x, 2)

numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]

krugi = map(krug, numbers)
print(*krugi, sep='\n')


def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

def sortirofka(number):
    if 99 < number < 1000:
        if number % 5 == 2:
            return number

def cube(number):
    return number**3

numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

total = filter(sortirofka, numbers)
total = map(cube, total)
print(*total, sep='\n')


def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc

def tot(x, y):
    return x+y**2

numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
total = reduce(tot, numbers, 0)
print(total)