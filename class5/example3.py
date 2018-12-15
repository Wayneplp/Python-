import turtle
t=turtle.Pen()
t.speed(1000)
for i in range(200):
    tup=(i/215.0,i/255.0,i/235.0)
    t.pencolor(tup)
    t.forward(i)
    t.left(61)
turtle.done()
