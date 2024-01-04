import random
import turtle
ısın=turtle.Turtle()
ısın.speed(0)
back=turtle.Screen()
back.bgcolor("black")

col=("white", "red", "yellow", "blue", "cyan", "green", "grey", "black")

for i in range(180):
    renk=random.randint(0,7)
    ısın.pencolor(col[renk])
    ısın.forward(100)
    ısın.right(30)
    ısın.forward(20)
    ısın.left(60)
    ısın.forward(50)
    ısın.right(30)
    
    ısın.penup()
    ısın.setpos(0,0)
    ısın.pendown()
    ısın.right(2)
    
turtle.done()
