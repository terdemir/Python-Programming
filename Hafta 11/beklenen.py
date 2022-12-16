import turtle
kalem=turtle.Turtle()
kalem.speed(10)

for i in range(180):
    kalem.forward(100)
    kalem.right(30)
    kalem.forward(20)
    kalem.left(60)
    kalem.forward(50)
    kalem.right(30)

    kalem.penup()
    kalem.setpos(0,0)
    kalem.pendown()
    kalem.right(2)

turtle.done()