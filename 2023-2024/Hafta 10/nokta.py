import turtle
kalem=turtle.Turtle()
kalem.dot()
kalem.forward(100)
kalem.right(90)
for i in range(10):
    kalem.dot()
    kalem.forward(10)

kalem.right(90)
kalem.up()
for i in range(10):
    kalem.dot()
    kalem.forward(10)

kalem.right()
for i in range(3):
    kalem.down()
    kalem.dot()
    kalem.forward(20)
    kalem.up()
    kalem.dot()
    kalem.forward(20)
    
turtle.done()
    