import turtle

t = turtle.Pen()
turtle.colormode(255)
t.pencolor(255,135,220)
for i in range(5):
    t.forward(i+10)
    t.left(90)
turtle.done()
