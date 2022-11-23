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