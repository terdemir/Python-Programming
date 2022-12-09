import turtle
kalem=turtle.Turtle()
kalem.pensize(5)
kalem.pencolor("blue")
for i in range(10):
    kalem.dot()
    kalem.forward(200)
    kalem.left(360/5)
turtle.done()
