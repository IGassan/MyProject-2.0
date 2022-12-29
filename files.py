n = input()
file = open(n)
print(*n)
file.close()


n = input()
file = open(n)
line = file.readlines()[-2]
print(line)
file.close()

import random

file = open('lines.txt', encoding='utf-8')
line = file.readlines()[random.randrange(list(line))]
print(line)
file.close()


file = open('numbers.txt', encoding='utf-8')
print(sum(map(int, file)))
file.close()


file = open('nums.txt', encoding='utf-8')
print(sum([int(i) for i in file.read().split()]))
file.close()


file = open('prices.txt')
lines = map(str.split, file)
print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
file.close()