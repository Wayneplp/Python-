import turtle
import antigravity

t = turtle.Pen()

t.speed(0)
t.pencolor('white')
turtle.bgcolor('black')

x = 0
t.penup()

t.right(45)
t.forward(90)
t.right(135)

t.pendown()
while x < 120:
    t.forward(200)
    t.right(61)
    t.forward(200)
    t.right(61)
    t.forward(200)
    t.right(61)
    t.forward(200)
    t.right(61)
    t.forward(200)
    t.right(61)
    t.forward(200)
    t.right(61)

    t.right(11.1111)
    x = x + 1
turtle.done()
