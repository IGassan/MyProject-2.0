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

