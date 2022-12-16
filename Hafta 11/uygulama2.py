import turtle
ucgen=turtle.Turtle()
ucgen.pencolor("purple")
ucgen.pensize(2)
ucgen.speed(6)
for i in range(25):
    ucgen.forward(i*20)
    ucgen.right(120)
turtle.done()