a = int(input())
num = 0
while a > 1:
    if a % 2 != 0:
        a += 1
    a /= 2
    num += 1
print(num)


en = [chr(x) for x in range(ord('a'), ord('z') + 1)]
res = ""
t = input().split()

for p in t:
    s = len(''.join(filter(str.isalpha, p)))
    for e in p:
        if e.isupper():
            res+=en[(s+en.index(e.lower()))%26].upper()
        elif e.islower():
            res+=en[(s+en.index(e))%26]
        else:
            res+=e
    res+=' '
print(res)


