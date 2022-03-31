import turtle

turtle.bgcolor('black')
turtle.title('My Graphics')


t = turtle.Turtle()

t.speed(2000)
t.pensize(2)
# t.color('yellow')
colours = ['blue', 'green', 'red']
for i in range(250):
    t.color(colours[i%3])
    t.forward(i*2)
    t.left(119)

turtle.done()