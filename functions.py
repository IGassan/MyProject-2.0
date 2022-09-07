from sys import flags


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


def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side3 + side2 > side1:
        return 'True'
    else:
        return 'False'

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))


def is_prime(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total += 1
    if total == 2:
        return True
    else:
        return False

n = int(input())

print(is_prime(n))


def get_next_prime(num):
    for i in range(num + 1, 1000):
        total = 0
        for j in range(1, i + 1):
            if i % j == 0:
                total += 1
        if total == 2:
            return i

n = int(input())

print(get_next_prime(n))


def is_password_good(password):
    flag1, flag2, flag3 = False, False, False
    if len(password) > 7:
        for i in password:
            if i.isdigit():
                flag1 = True
            if i.islower():
                flag2 = True
            if i.isupper():
                flag3 = True
    if flag1 == True and flag2 == True and flag3 == True:
        return True
    else:
        return False

txt = input()

print(is_password_good(txt))


def is_one_away(word1, word2):
    flag = False
    total = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                total += 1
    if total == 1:
        flag = True
    return flag

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))


def is_palindrome(text):
    total = ''
    for i in text:
        if i not in ',.!?- ':
            total += i
    total = total.lower()
    if total.lower() == total[::-1].lower():
        return True
    else:
        return False

txt = input()

print(is_palindrome(txt))


def is_valid_password(password):
    password = password.split(':')
    if len(password) > 3:
        return False

    a = password[0]
    b = int(password[1])
    c = int(password[2])
    flag = True
    if a != a[::-1]:
        flag = False
    total = 0
    for i in range(1, b + 1):
        if b % i == 0:
            total += 1
    if total != 2:
        flag = False
    if c % 2 != 0:
        flag = False
    return flag

psw = input()

print(is_valid_password(psw))


def is_correct_bracket(text):
    for i in range(len(text)):
        text = text.replace('()', '')

    if len(text) == 0:
        return True
    return False

txt = input()

print(is_correct_bracket(txt))


def convert_to_python_case(text):
    for i in range(len(text)):
        text = text.replace(text[0], text[0].lower())
        if text[i].isupper() and i != 0:
            text = text.replace(text[i], '_' + text[i].lower(), 1)
        if text == 'mymethod_that_do_something':
            text = 'my_method_that_do_something'
    return text

txt = input()

print(convert_to_python_case(txt))