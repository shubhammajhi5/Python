import turtle

turtle.bgcolor('black')
turtle.title('My Graphics')


t = turtle.Turtle()

t.speed(2000)
t.pensize(2)
t.color('green')
# colours = ['violet', 'blue', 'green', 'yellow', 'red']
for i in range(10):
    rad = 100
    for j in range(10):
        t.circle(rad)
        rad+=5
    t.left(36)

turtle.done()