countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
last = countries[-1]
print(last)


primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71) 
print(primes[:6])


countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[2:])


countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[:-3])


countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[3:8])


countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
number = len(countries)
print(number)


numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
total = min(numbers) + max(numbers)
print(total)


countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
index = countries.index('Slovenia')
print(index)


countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
number = countries.count('Spain')
print(number)


numbers1 = (1, 2, 3)
numbers2 = (6,)
numbers3 = (7, 8, 9, 10, 11, 12, 13)
total = numbers1 * 2 + numbers2 * 9 + numbers3
print(total)


city_name = input()
city_year = int(input())
city = (city_name, city_year)
print(city)


tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if len(i) > 0]
print(non_empty_tuples)


tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [i[:-1] + (100,) for i in tuples ]
print(new_tuples)


numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
total = 1
for i in numbers:
    total *= i
print(total)


data = 'Python для продвинутых!'
total =tuple(data)
print(total)


poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
poet_data = list(poet_data)
poet_data[2] = 'Москва'
poet_data = tuple(poet_data)
print(poet_data)


numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
total = []
for i in numbers:
    total.append(sum(i) / len(i))
print(total)


a, b, c = int(input()), int(input()), int(input())
total = ()
x = -(b / (2 * a))
y = (4 * a * c - b ** 2) / (4 * a)
total = (x, y)
print(total)


n = int(input())
spisok = ()
for i in range(n):
    spisok += (input().split(),)
for i in spisok:
    print(*i)
print()
for i in spisok:
    if int(i[1]) > 3:
        print(*i)


n = int(input())
total = [1, 1, 1]
a, b, c = 1, 1, 1
for i in range(0, n - 3):
    a, b, c = b, c, a + b + c
    total.append(c)
print(*total[:n])