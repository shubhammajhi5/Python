import turtle

turtle.bgcolor('black')
turtle.title('My Graphics')

t = turtle.Turtle()

t.speed(2000)
t.pensize(1)
t.color('orange')
# colours = ['blue', 'green','violet', 'red', 'indigo', 'yellow', 'orange' ]
for i in range(150):
    t.forward(i)
    t.right(160)
    for j in range(3):
        t.forward(i)
        t.right(190)

turtle.done()