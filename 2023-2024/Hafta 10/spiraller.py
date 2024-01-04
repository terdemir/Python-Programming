import turtle
spiral=turtle.Turtle()

back=turtle.Screen()
back.bgcolor("black")

spiral.speed(0)


col=("white", "red", "yellow")
for i in range (300):
    spiral.pencolor(col[i%3])
    spiral.forward(i*5)
    spiral.right(121)
    
turtle.done()
