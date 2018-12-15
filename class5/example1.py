import turtle
t=turtle.Pen()
t.speed(100)

turtle.bgcolor('black')
color=['red','green','yellow','orange','blue','pink']
for i in range(200):
    t.pencolor(color[i%6])
    t.width(i*6/200)
    t.forward(i)
    t.left(61)
    
turtle.done()
    
    
    
