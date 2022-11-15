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


import turtle

def sharik(numb):
    turtle.pensize(15)
    for _ in range(numb):
        turtle.dot()
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()

sharik(11)


import turtle

def rectangle(width, height):
  for _ in range(4):
    turtle.dot()
    turtle.forward(width)
    turtle.left(90)
    width, height = height, width

width = int(input())
height = int(input())
rectangle(width, height)


import turtle

turtle.shape('turtle')

def line(width):
    turtle.penup()
    turtle.forward(width)
    turtle.pendown()
    turtle.stamp()
    turtle.penup()
    turtle.backward(width)
turtle.stamp()

side = int(input())
for i in range(10):
    turtle.setheading(36 * i)
    line(side)


import turtle

def turtle_clock(turtles):
  turtle.Screen().bgcolor('skyblue')
  turtle.pensize(5)
  turtle.penup()
  turtle.shape('turtle')
  turtle.stamp()
  for _ in range(turtles):
    turtle.forward(95)
    turtle.pendown()
    turtle.forward(15)
    turtle.penup()
    turtle.forward(20)
    turtle.stamp()
    turtle.backward(130)
    turtle.left(360 / turtles)
    
turtle_clock(12)


import turtle
colors=['red', 'blue', 'yellow', 'green', 'purple', 'orange']
s=1
n=5
for i in range(8):
  for j in colors:
    turtle.pensize(s)
    turtle.pencolor(j)
    turtle.forward(n)
    turtle.left(45)
    n+=3
  s+=2


import turtle

def shalom(num):
  for _ in '123':
    turtle.forward(num)
    turtle.left(120)
  turtle.forward(num / 3)
  turtle.left(120)
  turtle.forward(num / 3 * 2)
  turtle.right(120)
  for _ in '123':
    turtle.forward(num)
    turtle.right(120)
  
shalom(100)

import turtle as t

t.color('green')

for i in range(-200, 200, 40):
    t.goto(i, -200)
    t.dot(10, 'blue')
    t.goto(0, 0)
    
t.color('red')
t.dot(15)  


import turtle

r = 50
pensize = 12
turtle.Screen().setup(600, 1000)
turtle.pensize(pensize)

points = {1: {"pos": (0, 0),      "color": "cyan"},
          3: {"pos": (r * 2, 0),  "color": "black"},
          4: {"pos": (r * 4, 0),  "color": "red"},
          5: {"pos": (r, -r),     "color": "yellow"},
          2: {"pos": (r * 3, -r), "color": "chartreuse"}}
             
for i in range(1, 6):
  turtle.penup()
  turtle.pencolor(points[i]["color"])
  turtle.goto(points[i]["pos"])
  turtle.pendown()
  turtle.circle(r - pensize / 2)


from turtle import *

def s(x): 
  down()
  circle(x)
  up()
  
Screen().setup(500, 500), speed(10), pensize(1.2) 
s(15), rt(90), down(), fd(90), up()  
goto(-88, -44), s(88 )
goto(-150, 17), s (150) 
goto(-90, 40), begin_fill(), s(15), end_fill() 
goto(60, 40), begin_fill(), s(15), end_fill() 
goto(-175, 150), s (40) 
goto(95, 150), s (40)


import turtle as t
import random as r
t.speed(0)
def ray(n):  
  t.left(45)
  for _ in range(3):
    t.forward(n)
    t.backward(n)
    t.right(45)
  t.left(90)
  t.forward(n)
  
def snow(n):
  for _ in range(8):
    for _ in range(4):
      ray(n)
    t.backward(4*n)
    t.right(45)

t.Screen().bgcolor('lightblue')
for _ in range(int(input())):
    t.Screen().setup(400, 400)
    t.penup()
    t.goto(r.randint(50, 300), r.randint(50, 300))
    t.pendown()
    #t.colormode(255)    
    t.pencolor(r.randint(0, 256), r.randint(0, 256), r.randint(0, 256))
    snow(r.randint(10, 50))