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