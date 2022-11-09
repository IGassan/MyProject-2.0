from decimal import Decimal

s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
numbers = [Decimal(i) for i in s.split()]

maximum = max(numbers)
minimum = min(numbers)
print(maximum + minimum)


from decimal import Decimal

s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
numbers = [Decimal(i) for i in s.split()]
total = sum(numbers)
numbers.sort(reverse=True)
print(total)
print(*numbers[:5])


from decimal import *

num = Decimal(input())
num_tuple = num.as_tuple()
maximum = max(num_tuple.digits)
minimum = min(num_tuple.digits)
if -1 < num < 1:
    minimum = 0
print(maximum + minimum)


from decimal import *

num = Decimal(input())
print(num.exp() + num.ln() + num.log10() + num.sqrt())


from fractions import Fraction

numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']

for i in numbers:
    print(i, '=', Fraction(i))


from fractions import Fraction

s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
numbers = [Fraction(i) for i in s.split()]
print(max(numbers) + min(numbers))


from fractions import Fraction

m = int(input())
n = int(input())
print(Fraction(m, n))


from fractions import Fraction

m = input()
n = input()
print(f'{m} + {n} = {Fraction(m) + Fraction(n)}')
print(f'{m} - {n} = {Fraction(m) - Fraction(n)}')
print(f'{m} * {n} = {Fraction(m) * Fraction(n)}')
print(f'{m} / {n} = {Fraction(m) / Fraction(n)}')


from fractions import Fraction

total = [Fraction(1, i**2) for i in range(1, int(input()) + 1)]
print(sum(total))


from fractions import Fraction
from math import factorial

total = [Fraction(1, factorial(i)) for i in range(1, int(input()) + 1)]
print(sum(total))


from fractions import Fraction as F
from math import gcd

n = int(input())
a = n // 2
b = n - a
while gcd(a, b) != 1:
    a -= 1
    b += 1
print(F(a, b))


from fractions import Fraction

total = set()
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n):
        if Fraction(j, i) < 1:
            total.add(Fraction(j, i))
print(*sorted(total), sep='\n')