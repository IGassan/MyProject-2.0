import turtle

def rectangle(width, height):
  for _ in range(4):
    turtle.forward(width)
    turtle.left(90)
    width, height = height, width

width = int(input())
height = int(input())
rectangle(width, height)


import turtle

def triangle(side):
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)

side = int(input())
triangle(side)


import turtle

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

side = int(input())
for i in range(1, 4):
    turtle.setheading(22.5 * i)
    square(side)


import turtle

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

side = int(input())
for i in range(8):
    turtle.setheading(45 * i)
    square(side)


import turtle

def triangle(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)

side = int(input())
triangle(side)


import turtle

def hexagon(side):
  for _ in '1' * 6:
    turtle.forward(side)
    turtle.right(60)
    
def count(size, num):
  for _ in range(num):
    hexagon(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.left(60)
    
count(60, 6)


import turtle

def rectangle(width, height):
    turtle.forward(width)
    turtle.left(120)
    turtle.forward(width)
    turtle.left(60)
    turtle.forward(width)
    turtle.left(120)
    turtle.forward(width)
    turtle.left(60)

width = int(input())
height = int(input())
rectangle(width, height)


import turtle

def rectangle(width):
    turtle.forward(width)
    turtle.left(60)
    turtle.forward(width)
    turtle.left(120)
    turtle.forward(width)
    turtle.left(60)
    turtle.forward(width)
    turtle.left(120)

side = int(input())
for i in range(9):
    turtle.setheading(40 * i)
    rectangle(side)


import turtle

def line(width):
    turtle.forward(width)
    turtle.backward(width)

side = int(input())
for i in range(12):
    turtle.setheading(30 * i)
    line(side)


import turtle

def square(side):
    for _ in range(5):
        turtle.forward(side)
        turtle.right(144)

side = int(input())
square(side)


import turtle

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

for i in range(15):
    square(40 + (i *10))


import turtle

def square(side):
    turtle.forward(side)
    turtle.left(90)

for i in range(40):
    square(5 + (i * 5))