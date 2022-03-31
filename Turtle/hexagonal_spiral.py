import turtle

turtle.bgcolor('black')
turtle.title('My Graphics')


t = turtle.Turtle()

t.speed(2000)
t.pensize(2)
# t.color('yellow')
colours = ['violet', 'blue', 'green', 'yellow', 'orange', 'red']
for i in range(200):
    t.color(colours[i%6])
    t.forward(i*1.5)
    t.left(59)

turtle.done()