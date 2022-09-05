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