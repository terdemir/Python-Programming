#Örnek 1
isim=input("İsminizi giriniz")
print("Merhaba", isim)

#Örnek 2
a=input("Birinci sayıyı giriniz")
b=input("İkinci sayıyı giriniz")
toplam=a+b
print("Girdiğiniz sayıların toplamı=", a+b)
print("Girdiğiniz sayıların toplamı=", toplam)

a=int(a)
b=int(b)
toplam=a+b
print("Girdiğiniz sayıların toplamı=", a+b)
print("Girdiğiniz sayıların toplamı=", toplam)

#Örnek 3
vize=int(input("Vize notunu giriniz"))
final=int(input("Final notunu giriniz"))
ortalama=(vize*40/100)+(final*60/100)
print(ortalama)
print(ortalama>=60)