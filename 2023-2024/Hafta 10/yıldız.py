import turtle
import random

def renkuret():
    renk="#"
    for i in range(6):
        renk=renk+random.choice("ABCDEF1234567890")
    return renk

kalem=turtle.Turtle()
kalem.pencolor("Yellow")
kalem.pensize(5)
kalem.speed(10)
for i in range(18):
    
    for i in range(5):
        kalem.dot()
        kalem.right(144)
        kalem.forward(200)
    renk=renkuret() 
    kalem.pencolor(renk)   
    kalem.right(20)


turtle.done()