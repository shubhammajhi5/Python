import turtle

turtle.bgcolor('white')
turtle.title('My Graphics')

t = turtle.Turtle()

t.speed(5)
t.pensize(2)
t.color('black')


'''TOP PORTION'''
t.fillcolor('orange')
t.begin_fill()
t.penup()
t.goto(-600,100)
t.pendown()
for i in range(2):
    t.forward(1200)
    t.left(90)
    t.forward(200)
    t.left(90)
t.penup()
t.goto(0,0)
t.pendown()
t.end_fill()


'''MIDDLE PORTION'''
t.fillcolor('white')
t.begin_fill()
t.penup()
t.goto(-600,100)
t.pendown()
for i in range(2):
    t.forward(1200)
    t.right(90)
    t.forward(200)
    t.right(90)
t.penup()
t.goto(0,0)
t.pendown()
t.end_fill()


'''BOTTOM PORTION'''
t.fillcolor('green')
t.begin_fill()
t.penup()
t.goto(-600,-100)
t.pendown()
for i in range(2):
    t.forward(1200)
    t.right(90)
    t.forward(200)
    t.right(90)
t.penup()
t.goto(0,0)
t.pendown()
t.end_fill()


'''CHAKRA'''
t.pensize(2)
t.color('blue')
t.speed(10)

for i in range(24):
    t.forward(75)
    t.setposition(0,0)
    t.left(15)

t.setposition(0,-75)
t.pensize(5)
t.circle(75)


turtle.done()