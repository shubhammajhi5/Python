import turtle
from random import randint

turtle.bgcolor('black')
turtle.title('My Graphics')

t = turtle.Turtle()

t.speed(100)

for i in range(5):
    for x in range(10):
        t.speed(x*10)
        for j in range(2):
            turtle.colormode(255)
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            t.color(r, g, b)
            t.pensize(2)
            t.circle(80+i*20, 90)
            t.left(90)
        t.left(45)
    t.pensize(i/20+i)
    

turtle.done()