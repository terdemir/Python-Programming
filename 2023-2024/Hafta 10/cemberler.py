import random
import turtle

kalem=turtle.Turtle()
def renkuret():
    renk="#"
    for i in range(6):
        renk=renk+random.choice("ABCDEF1234567890")
    return renk
kalem.pencolor("green")
kalem.pensize(3)
kalem.speed(10)

for i in range(12):
    kalem.circle(100)
    kalem.right(30)
    renk=renkuret()
    kalem.pencolor(renk)

turtle.done()