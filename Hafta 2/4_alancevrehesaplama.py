from cgi import print_arguments


print("Yarıçapı 5 olan dairenin alanı ve çevresini hesaplayan python kodlarını yazınız.")

#Dairenin alanı pi.r.r dir. çevresi 2.pi.r dir. 
pi=3.14
r=5
print("pi'nin veri tipi:", type(pi), "dir")
print("r'nin veri tipi:", type(r), "dir")

cevre=2*pi*r
alan=pi*r*r

print("Çevre=", cevre)
print("Alan=", alan)

print(type(cevre))
print(type(alan))

print("Bu dairenin çevresi=", 2*pi*r)
print("Bu dairenin alanı=", pi*r*r)
