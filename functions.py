def draw_box():
    print('*' * 10)
    for i in range(12):
        print('*' + ' ' * 8 + '*')
    print('*' * 10)

draw_box()


def draw_triangle():
    for i in range(1, 11):
        print('*' * i)

draw_triangle()


def draw_triangle(fill, base):
    for i in range(1, base + 1):
        print(fill * min(i, base - i + 1))

fill = input()
base = int(input())

draw_triangle(fill, base)


def print_fio(name, surname, patronymic):
    print((surname[0] + name[0] + patronymic[0]).upper())

name, surname, patronymic = input(), input(), input()

print_fio(name, surname, patronymic)


def print_digit_sum(num):
    total = 0
    while num > 0:
        number = num % 10
        total += number
        num //= 10
    print(total)

n = int(input())

print_digit_sum(n)


def convert_to_miles(km):
    return km * 0.6214

num = int(input())

print(convert_to_miles(num))


def get_days(month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 28

num = int(input())

print(get_days(num))


def get_factors(num):
    total = list()
    for i in range(1, num + 1):
        if num % i == 0:
            total.append(i)
    return total    

n = int(input())

print(get_factors(n))


def number_of_factors(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total += 1
    return total  

n = int(input())

print(number_of_factors(n))


def find_all(target, symbol):
    total = list()
    for i in range(len(target)):
        if target[i] == symbol:
            total.append(i)
    return total    

s = input()
char = input()

print(find_all(s, char))


def merge(list1, list2):
    return sorted(list1 + list2)

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))


def quick_merge(list1, list2):
    result = []

    p1 = 0
    p2 = 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result

total_list = []
for i in range(int(input())):
    num = [int(q) for q in input().split()]
    total_list = quick_merge(total_list, num)

print(*total_list)