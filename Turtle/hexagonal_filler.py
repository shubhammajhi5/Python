import turtle

turtle.bgcolor('black')
turtle.title('My Graphics')


t = turtle.Turtle()

t.speed(2000)
# t.pensize(2)
# t.color('yellow')
colours = ['violet', 'blue', 'green', 'yellow', 'red']
for i in range(200):
    t.color(colours[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)

turtle.done()