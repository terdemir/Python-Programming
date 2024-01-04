#kullanıcının girdiği metni kullanıcının girdiği sayıda ekrana yazdırınız.

metin=input("Metni giriniz: ")
tekrar=int(input("tekrar sayısını giriniz: "))
for i in range(tekrar):
    print(metin)


#kullanıcının girdiği sayının faktoriyelini buldurunuz.

sayi=int(input("1 sayı giriniz: "))
faktoriyel=1
for i in range(1,sayi+1):
    faktoriyel*=i

print(faktoriyel)