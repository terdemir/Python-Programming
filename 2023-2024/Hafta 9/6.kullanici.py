import turtle
kalem=turtle.Turtle()

uzunluk=int(input("Uzunluğu giriniz: "))
aci=int(input("Açıyı giriniz: "))

kalem.right(aci)
kalem.forward(uzunluk)

turtle.done()