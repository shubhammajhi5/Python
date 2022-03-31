import turtle

turtle.bgcolor('black')
turtle.title('My Graphics')


t = turtle.Turtle()

t.speed(2000)
t.pensize(1)
t.color('yellow')
# colours = ['violet', 'blue', 'green', 'yellow', 'orange', 'red']
for i in range(200):
    t.circle(i)
    t.left(5)

turtle.done()