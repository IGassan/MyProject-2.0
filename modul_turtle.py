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


from turtle import *

for n, l, r, c in [(3, 120, 150, (185, 122, 87)), (4, 90, 110, (0, 162, 232))]:
  hideturtle()
  fillcolor(c)
  begin_fill()
  for _ in range(n):
    forward(r)
    lt(l)
  end_fill()
  forward(20)
  rt(90)


import turtle as t
col = ['red', 'yellow', 'lime']
t.hideturtle()
t.begin_fill()
t.goto(-60, 150)
t.goto(60, 150)
t.goto(60, -150)
t.goto(-60, -150)
t.goto(-60, 150)
t.end_fill()
t.up()
for i in range(3):
  t.goto(0, 90 - i * 90)
  t.dot(80, col[i])


import turtle
turtle.speed(5)

for _ in range(3):
    turtle.forward(90)
    turtle.left(120)

turtle.penup()
turtle.goto(0, 60)

turtle.color('white')
turtle.fillcolor('white')
turtle.begin_fill()
for _ in range(3):
    turtle.forward(90)
    turtle.color('black')
    turtle.dot(30)
    turtle.color('white')
    turtle.right(120)

turtle.end_fill()


import turtle

def rainbow_circle(radius):
  """draws rainbow circle of custom size"""
  
  colors = ("#FF0000", "#FFA600", "#FFFF00", "#62FF00", "#89F590", "#69C5FF", 
  "#1E56FC","#4800FF","#CC00FF","#FF5099")
  turtle.hideturtle()
  
  for i in range(10):
    turtle.dot(radius - (radius / 10) * i, colors[i])

rainbow_circle(300)


import turtle as t
t.Screen().setup(380, 480)
t.Screen().bgcolor(2, 27, 157)
t.pensize(150)
t.color(255, 180, 0)
t.dot()
t.forward(30)
t.color(2, 27, 157)
t.dot()


import turtle as t
t.Screen().setup(380, 480)
t.Screen().bgcolor(2, 27, 157)
t.pensize(150)
t.color(255, 180, 0)
t.dot()
t.forward(30)
t.color(2, 27, 157)
t.dot()


import turtle
turtle.Screen().bgcolor('blue')
moon = turtle.Turtle()
moon.hideturtle()
moon.pencolor('orange')
moon.dot(200)
shadow = {0: turtle.Turtle(), 5: turtle.Turtle()}
for i in [0, 5]:
  shadow[i].hideturtle()
  shadow[i].pencolor('blue')
  shadow[i].penup()
while 1:
  for i in range(200, -201, -5):
    shadow[i % 10].goto(i, 0)
    shadow[i % 10].dot(200)
    shadow[(i + 5) % 10].clear()


import turtle, random

turtle.speed(0)
turtle.Screen().bgcolor('black')
turtle.up()
def star(size, x, y):
  turtle.goto(x, y)
  turtle.left(random.randint(0, 360))
  for _ in range(5):
    turtle.forward(size)
    turtle.right(144)

def play():
  for i in range(random.randint(50, 200)):
    side = random.randint(5, 20)
    x, y = (random.randint(-150, 150) for _ in '12')
    color = tuple(random.randint(0, 255) for _ in '123')
    turtle.fillcolor(color)
    turtle.begin_fill()
    star(side, x, y)
    turtle.end_fill()

play()


import turtle as t
import math as m
import random as r

def figure(n, square):
  size = (square * 4 * m.tan(m.radians(180 / n)) / n) ** 0.5
  color = tuple((r.randint(0, 255) for _ in range(3)))
  t.fillcolor(color)
  t.begin_fill()
  
  t.forward(size / 2)
  t.left(360 / n)
  for i in range(n - 1):
    t.forward(size)
    t.left(360 / n)
  t.forward(size / 2)
  t.end_fill()
  
def main():
  t.speed(0)
  t.hideturtle()
  for y in range(130, -200, -75):
    for x in range(-150, 170, 75):
      t.penup()
      t.goto(x, y)
      t.pendown()
      figure(r.randint(3, 6), 1800)
    
main()


import turtle

def sq(side, color):
  turtle.fillcolor(color)
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(side)
    turtle.right(90)
  turtle.end_fill()

side = 50
n = 8
canvx = 400 
canvy = 400
turtle.Screen().setup(canvx, canvy)
turtle.speed(0)
positionx = -(canvx // 2)
positiony = canvy // 2
turtle.penup()
turtle.goto(positionx, positiony)
turtle.pendown()
colors = ['black', 'white']
for j in range(n):
  for i in range(n):
    sq(side, colors[(i + j)% 2])
    turtle.forward(side)
  positiony -= side
  turtle.penup()
  turtle.goto(positionx, positiony)
  turtle.pendown()


import turtle as t, math

t.Screen().bgcolor('black')
colors = ['#ffff66','#ad5a00','#fd5a0A', 'cyan',
'#FF6347','#ad5a00','#ad5a00','#20B2AA', '#4169E1','#ad5a00']
f = ('Times New Roman', 11, 'normal')
lst = [[(-150, 0), (-170, -20)], [(-80, 80), (-100, 60)],
[(-40, 20), (-60, 5)], [(-80, -100), (-100, -120)], [(0, -120), (-10, -135)],
[(60, 60), (40, 40)], [(110, -100), (90, -120)]]

circ = [50, 10, 20, 15, 12, 40, 45]
plan = ['Солнце', 'Меркурий', 'Венера', 'Эемля', 'Марс', 'Юпитер', 'Сатурн']
i = 0
t.up()
for a, b in lst:
  t.goto(a)
  t.fillcolor(colors[i])
  t.begin_fill()
  t.circle(circ[i])
  t.end_fill()
  t.goto(b)
  t.fillcolor('white')
  t.write(plan[i], font=f)
  i += 1

t.goto(110, -85)
t.pensize(5)
t.down()
t.pencolor('blue')
a, b = 70, 30
dx = t.xcor()
dy = t.ycor()
for deg in range(361):
    rad = math.radians(deg)
    x = a * math.sin(rad) + dx
    y = -b * math.cos(rad) + b + dy
    t.goto(x, y)


import turtle, math

turtle.speed(0)
def figure(n, side, color):
  s = 180 - 180 * (n - 2) / n
  turtle.fillcolor(color)
  turtle.begin_fill()
  for i in range(n):
    turtle.forward(side)
    turtle.right(s)
  turtle.end_fill()

turtle.up()
turtle.goto(0, 100)
figure(8, 100, 'black')
turtle.goto(3, 94)
figure(8, 95, 'white')
turtle.goto(6, 88)
figure(8, 90, 'red')

turtle.goto(-50, -50)
turtle.fillcolor('white')
turtle.begin_fill()
turtle.write('STOP', font=('Arial', 57, 'bold'))
turtle.end_fill()


import turtle as t
from random import *
t.Screen().setup(400,400)
t.Screen().bgcolor('#08204E')
t.speed(10)
t.tracer(20)
def zvezdi():
  for i in range(60):
    t.up()
    r=randint(1,5)
    n=randint(0,360)
    t.goto(randint(-200,200),randint(-200,200))
    t.left(n)
    t.down()
    t.pencolor('white')
    t.begin_fill()
    t.fillcolor('white')
    for i in range(5):
      t.forward(r)
      t.left(144)
    t.end_fill()

def zdania():
  od=-200
  while od<200:
    t.pencolor('blue')
    t.up()
    v=randrange(-135,76,15)  #Кр высоты зд
    d=randrange(35,81,15)    #Длинна зд
    od=od+d                  #Кр длинны зд
    t.goto(od,-200)
    t.down()
    t.begin_fill()
    t.fillcolor('blue')
    t.goto(od,v)
    t.goto(od-d,v)
    t.goto(od-d,-200)
    t.end_fill()
    #Теперь окна
    visota_schet=0  #Счетчик размера по высоте 
    t.up()
    t.goto(od-d+5,v-15)
    t.setheading(0)
    schet=5    #Счетчик размера по длине
    while visota_schet!=v+195:
      okna=randint(1,20)        #Одно окно из 20 горит
      t.down()
      t.begin_fill()
      if okna==5:
        t.pencolor('yellow')
        t.fillcolor('yellow')
      else:
        t.pencolor('#254AC7')
        t.fillcolor('#254AC7')
        
      for i in range(4):
        t.forward(10)
        t.left(90)
      t.end_fill()
      t.up()
      t.forward(15)
      schet+=15       #Счетчик размера по длине 
      if schet==d:
        schet=5
        visota_schet+=15
        t.goto(od-d+5,v-15-visota_schet)
        t.setheading(0)
        
zvezdi()
t.tracer(30)
zdania()


import turtle
from math import cos,sin,pi
turtle.hideturtle()
a = 2*pi
t = 0
turtle.fillcolor("red")

turtle.begin_fill()
while t < a:
  x = 128 * sin(t)**3
  y = 8 * (13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t)-5)
  turtle.goto(x,y)
  t += 0.01
turtle.end_fill() 


from turtle import *
from random import *
speed(0)
def stars(size, count, colo, x,y):
  for i in range(count):
    h = tuple(randint(0, 255) for _ in '123')
    size = randint(3,33)
    fillcolor(h)
    color(h)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(5):
      forward(size)
      left(144)
    end_fill()
size = randint(10,20)
count = randint(50,80)
h = tuple(randint(0, 255) for _ in '123')

def left_mouse_click(x, y):
    stars(1,1,h,x, y)
hideturtle()
Screen().bgcolor('black')
Screen().onclick(left_mouse_click)
Screen().listen()