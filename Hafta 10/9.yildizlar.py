import turtle
kalem=turtle.Turtle()
kalem.pencolor("grey")
kalem.pensize(2)
kalem.speed(10)
for i in range(18):
    for i in range(5):
        kalem.dot()
        kalem.right(144)
        kalem.forward(200)
    kalem.right(20)
turtle.done()
