my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
print(min(my_dict) + max(my_dict))


users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

total = list()
for i in users:
    if i['phone'][-1] == '8':
        total.append(i['name'])
print(*sorted(total))


users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

total = list()
for i in users:
    if 'email' not in i or i['email'] == '':
        total.append(i['name'])
print(*sorted(total))


n = input()
my_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
total = list()
for i in n:
    total.append(my_dict[i])
print(total)


n = input()
d = {
    "CS101": "3004, Хайнс, 8:00",
    "CS102": "4501, Альварадо, 9:00",
    "CS103": "6755, Рич, 10:00",
    "NT110": "1244, Берк, 11:00",
    "CM241": "1411, Ли, 13:00"
}
print(f'{n}: {d[n]}')


n = input().upper()
d={".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
    "A":'2', "B":'22', "C":'222',
    "D":'3', "E":'33', "F":'333',
    "G":'4', "H":'44', "I":'444',
    "J":'5', "K":'55', "L":'555',
    "M":'6', "N":'66', "O":'666',
    "P":'7', "Q":'77', "R":'777', "S": '7777',
    "T":'8', "U":'88', "V":'888',
    "W":'9', "X":'99', "Y":'999', "Z": '9999',
    " ":'0', '"':''
}
total = list()
for i in n:
    total.append(d[i])
print(*total, sep='')


n = input().upper()
letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
total = dict(zip(letters, morse))
totol = list()
for i in n:
    if i in letters:
        totol.append(total[i])
print(*totol)


result = {}
for i in range(1, 16):
    result[i] = i ** 2


dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
result.update(dict1)
for i, j in dict2.items():
    result[i] = result.get(i, 0) + j


text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for i in text:
    result[i] = result.get(i, 0) + 1


s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
result1 = {}
result2 = {}
numbers = [c for c in s.split()]
for num in numbers:
    result1[num] = result1.get(num, 0) + 1
mx = (max(result1.values()))
for key, value in result1.items():
    if value == mx:
        result2[key] = result2.get(key, value)
mx2 = (min(result2))
print(mx2)

s = set(s.split())
print(s)


pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for name in pets:
    result[name[1:4]] = result.get((name[1:4]), []) + [name[0]]
print(result)


lst = [word.strip('.,!?:;-') for word in input().lower().split()]
result = {}
for word in lst:
    result[word] = result.get(word, 0) + 1
for key, values in sorted(result.items()):
    if values == min(result.values()):
        print(key)
        break


lst = input().split()
res = {}
for c in lst:
    if c in res:
        print(f'{c}_{res[c]}', end=' ')
    else:
        print(c, end=' ')
    res[c] = res.get(c, 0) + 1


n = int(input())
keys = []
values = []
for i in range(n):
    a = input().split(':')
    keys.append(a[0].lower())
    values.append(a[1].strip())
res = dict(zip(keys, values))
m = int(input())
for i in range(m):
    d = input().lower()
    final = res.get(d, 'Не найдено')
    print(final)


word1 = {}
word2 = {}
for i in input():
    word1[i] = word1.get(i, 0) + 1
for i in input():
    word2[i] = word2.get(i, 0) + 1
if word1 == word2:
    print('YES')
else:
    print('NO')


word1 = {}
word2 = {}
for i in input().lower():
    if i not in '.,!?:;- ':
        word1[i] = word1.get(i, 0) + 1
for i in input().lower():
    if i not in '.,!?:;- ':
        word2[i] = word2.get(i, 0) + 1
if word1 == word2:
    print('YES')
else:
    print('NO')


mydict = {}
for _ in range(int(input())):
    key, value = input().split(': ')
    mydict[key] = value
total = input()
for key, value in my_dict.items():
    if key == total:
        print(value)
    elif value == total:
        print(key)


mydict = {}
for _ in range(int(input())):
    key, *value = input().split()
    my_dict[key] = value
print(mydict)
m = int(input())
for i in range(m):