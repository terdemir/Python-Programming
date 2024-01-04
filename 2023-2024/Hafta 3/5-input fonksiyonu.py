isim=input("İsminizi Giriniz")
print("Merhaba ", isim)

a=input("Birinci sayıyı giriniz")
b=input("İkinci sayıyı giriniz")
Toplam=a+b
print("Girdiğiniz sayıların toplamı=", Toplam)

#input ile alınan değerler string türdedir. Bu nedenle sayısal değerler integera çevrilmelidir. 
a=int(a)
b=int(b)
Toplam=a+b
print("Girdiğiniz sayıların toplamı=", Toplam)


vize=int(input("Vize notunu giriniz"))
final=int(input("Final notunu giriniz"))

ortalama=(vize*40/100)+(final*60/100)
print(ortalama)
print(ortalama>=60)





