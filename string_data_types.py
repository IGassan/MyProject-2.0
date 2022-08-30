from itertools import count
from re import A


s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-10])

x = input()
for i in range(0, len(x), 2):
    print(x[i])

s=input()
for i in range(1,len(s)+1):
    print(s[-i])

total = ''
for i in range(3):
    x = input()
    total += x[0]
print(total[1] + total[0] + total[2])

x = input()
total = 0
for i in range(len(x)):
    total += int(x[i])
print(total)

x = input()
flag = False
for i in range(len(x)):
    if x[i] in '0123456789':
        flag = True
if flag == True:
    print('Цифра')
else:
    print('Цифр нет')

x = input()
totalplus = 0
totalproiz = 0
for i in range(len(x)):
    if x[i] == '+':
        totalplus += 1
    if x[i] == '*':
        totalproiz += 1
print('Символ + встречается', totalplus, 'раз')
print('Символ * встречается', totalproiz, 'раз')

x = input()
total = 0
for i in range(len(x) - 1):
    if x[i] == x[i + 1]:
        total += 1
print(total)

x = input()
totalglas = 0
totalsogl = 0
for i in range(len(x)):
    if x[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        totalglas += 1
    if x[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        totalsogl += 1
print('Количество гласных букв равно', totalglas)
print('Количество согласных букв равно', totalsogl)

x = int(input())
total = ''
while x > 0:
    total += str(x % 2)
    x //= 2
print(total[::-1])

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])

x = input()
if x == x[::-1]:
    print('YES')
else:
    print('NO')

x = input()
print(len(x))
print(x * 3)
print(x[0])
print(x[:3])
print(x[-3:])
print(x[::-1])
print(x[1:-1])

x = input()
print(x[2])
print(x[-2])
print(x[:5])
print(x[:-2])
print(x[::2])
print(x[1::2])
print(x[::-1])
print(x[len(x)::-2])

x = input()
if len(x) % 2 == 1:
    print(x[len(x) // 2 + 1:] + x[:len(x)// 2 + 1])
else:
    print(x[len(x) // 2:] + x[:len(x)// 2])

x = input()
if x == x.title():
    print('YES')
else:
    print('NO')

x = input()
print(x.swapcase())

x = input()
if 'хорош' in x.lower():
    print('YES')
else:
    print('NO')

x = input()
total = 0
for i in range(len(x)):
    if x[i] in 'abcdefghijklmnopqrstuvwxyz':
        total += 1
print(total)

x = input()
print(x.count(' ') + 1)

x = input()
x = x.lower()
print('Аденин:', x.count('а'))
print('Гуанин:', x.count('г'))
print('Цитозин:', x.count('ц'))
print('Тимин:', x.count('т'))

x = int(input())
total = 0
for i in range(x):
    y = input()
    if y.count('11') > 2:
        total += 1
print(total)

x = input()
total = 0
for i in range(len(x)):
    if x[i] in '0123456789':
        total += 1
print(total)

x = input()
if x.endswith('.com') or x.endswith('.ru'):
    print('YES')
else:
    print('NO')

x = input()
total = 0
maxim = 0
for i in x:
    if x.count(i) >= total:
        total = x.count(i)
        maxim = i
print(maxim)

x = input()
if x.count('f') > 1:
    print(x.find('f'), x.rfind('f'))
elif x.count('f') == 1:
    print(x.find('f'))
else:
    print('NO')

x = input()
print(x[:x.find('h')] + x[x.rfind('h') + 1:])

age = 2010
number = 10
print('In {}, someone paid {}k Bitcoin for two pizzas.'.format(age, number))

year = 2010
amount = '10K'
currency = 'Bitcoin'
print(f'In {year}, someone paid {amount} {currency} for two pizzas.')

x = int(input())
y = int(input())
for i in range(x, y + 1):
    print(chr(i), end=' ')

x = input()
for i in range(len(x)):
    print(ord(x[i]), end=' ')

y = int(input())
x = input()
for i in x:
    i = ord(i) - y
    if i < 97:
        i = 122 - (96 - i)
    print(chr(i), end="")

# Итоговая работа

s = 'Python rocks!'
print(len(s))

s = 'Python rocks!'
print(s[3])

s = 'Python rocks!'
print(s[1:5])

s = '    Python rocks!     '
print(s.strip())

s = 'Python rocks!'
print(s.upper())

s = input()
for i in range(len(s)):
    if i % 3 == 0:
        continue
    print(s[i], end='')

s = input()
print(s.replace('1', 'one'))

s = input()
print(s.replace('@', ''))

s = input()
total = 0
if s.count('f') > 1:
    print(s.find('f', s.find('f') + 1, len(s)))
elif s.count('f') == 1:
    print(-1)
else:
    print(-2)