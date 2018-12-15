import turtle
import random

t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
x = 1

while x < 800:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.colormode(255)

    t.pencolor(r, g, b)
    t.forward(x)
    t.right(90.911)

    x = x + 1

turtle.done()
