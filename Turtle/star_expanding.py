import turtle

turtle.bgcolor('black')
turtle.title('My Graphics')

t = turtle.Turtle()

t.speed(2000)
t.pensize(1)
t.color('red')
# colours = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red' ]
for i in range(125):
    # t.color(colours[i%7])
    t.forward(i*5)
    t.right(160)

turtle.done()