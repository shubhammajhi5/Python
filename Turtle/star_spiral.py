import turtle

turtle.bgcolor('black')
turtle.title('My Graphics')

t = turtle.Turtle()

t.speed(5000)
t.pensize(1)
t.color('orange')

for j in range(10, 250, 2):

    for i in range(5):
        t.forward(j*2)
        t.left(144)
    
    t.left(3)


turtle.done()