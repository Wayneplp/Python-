import turtle
t=turtle.Pen()
a=['red','green','blue']
x={'red':[0.93,0.79,0],'green':[0.3,1,0.7],'blue':[0.6,0.15,0.8]}
for i in range(200):
    t.pencolor(x[a[i%3]])
    t.forward(i)
    t.left(61)
turtle.done()
    
    
