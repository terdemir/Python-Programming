import turtle
spiral=turtle.Turtle()
back=turtle.Screen()
back.bgcolor("black")
spiral.speed(10)

col=("white", "pink", "cyan")
for i in range(300):
    spiral.pencolor(col[i%3])
    spiral.forward(i*4)
    spiral.right(121)
