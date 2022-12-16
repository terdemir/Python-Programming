import turtle
ciz=turtle.Turtle()
ciz.speed(10)
ciz.pencolor("red")
ciz.forward(100)
ciz.backward(200)
ciz.setpos(0,0)
ciz.right(60)
ciz.forward(100)
ciz.backward(200)
ciz.setpos(0,0)
ciz.right(60)
ciz.forward(100)
ciz.backward(200)
ciz.setpos(0,0)
ciz.left(120)
x=20
y=0
ciz.setpos(x,0)
ciz.left(120)
for i in range (10):
    for i in range(6):
        ciz.forward(x)
        ciz.left(360/6)
    x=x+10
    ciz.setpos(x,0)
turtle.done()