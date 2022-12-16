import turtle
isin=turtle.Turtle()
isin.pensize(2)
isin.speed(5)
isin.pencolor("pink")
for i in range(36):
    isin.forward(100)
    isin.backward(100)
    isin.left(10)

isin.pencolor("orange")
isin.setpos(100,100)
for i in range(36):
    isin.forward(100)
    isin.backward(100)
    isin.left(10)

isin.pencolor("blue")
isin.setpos(-100,100)
for i in range(36):
    isin.forward(100)
    isin.backward(100)
    isin.left(10)
isin.pencolor("green")
isin.setpos(0,200)
for i in range(36):
    isin.forward(100)
    isin.backward(100)
    isin.left(10)
turtle.done()