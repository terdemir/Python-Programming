import turtle
kalem=turtle.Turtle()
for i in range(10):
    kalem.dot()
    kalem.forward(10)
kalem.left(90)
kalem.up()      #noktalar arası çizgileri kaldırır.
for i in range(10):
    kalem.dot()
    kalem.forward(10)
kalem.left(90)
      #noktalar arası çizgileri koyar
for i in range(3):
    kalem.down()
    kalem.dot()
    kalem.forward(20)
    kalem.up()
    kalem.dot()
    kalem.forward(20)
turtle.done()