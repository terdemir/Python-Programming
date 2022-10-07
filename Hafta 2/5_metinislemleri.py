metin1="merhaba"
metin2="python"


print(metin1)
print(metin1+metin2)
print(metin1+" "+ metin2)
print(metin1*4)
print("metin1 değişkeninin uzunluğu=", len(metin1)) # len komutu bir değişkenin kaç karakterden oluştuğunu verir. 
print("metin1 değişkeninin türü=", type(metin1)) #type komutu bir değişkenin tipini verir.

metin3=metin1+" "+metin2
print(metin3)

print(metin3[0])   #Metnin ilk karakterini yazdırır.
print(metin3[3:8]) #Metnin 4, 5, 6, 7. karakterlerini yazdırır.
print(metin3[7::]) #8. karakterden sona kadar yazdırır.
print(metin3[-2])  #Sondan 2. karakteri yazdırır. 
print(metin3[:7])  #baştan 7. karaktere kadar yazdırır. indis değeri 0 dan 7 ye kadar olanlar
print(metin3[8:])  # Verilen başlangıç indisinden sonraki kararkteleri yazdırır
print(metin3[0:8:2]) #0, 2, 4 ve 6 numaralı indisleri dilimleyerek yazar.


#Veri tiplerini dönüştürme
a='5'
b='4'

print(a+b)
print(int(a)+int(b))

a=int(a)
b=int(b)
print(a+b)


