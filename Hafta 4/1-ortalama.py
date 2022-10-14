sinav1=int(input('1. sınav giriniz:'))
sinav2=int(input('2. sınav giriniz:'))
sinav3=int(input('3. sınav giriniz:'))
ortalama=(sinav1+sinav2+sinav3)/3
print("Ortalama=", ortalama)

if(ortalama>=50):
    print("Geçti")
if(ortalama<50):
    print("Kaldı")
print("Sonuçlandırıldı")
