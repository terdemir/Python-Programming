metin1="Merhaba"
metin2="Python"

print(metin1)
print(metin1+metin2)
print(metin1," ",metin2)
print(metin1+" "+metin2)

print((metin1+"\n")*5)
print("metin1 değişkeninin uzunluğu= ", len(metin1))
print("metin1 değişkeninin türü= ", type(metin1))

metin3=metin1+" "+metin2+" Programlama"
print(metin3)


print(metin3[0]) # metnin ilk karakterini yazdırır.
print(metin1[3:5]) # 4 ile 6. karakter arasını yazdır. 3 ile 6 yı yazmaz
print(metin3[6::]) #7. karakter ve sonrasını yazdır.
print(metin1[-2]) # sondan 2. karakteri yazdıdır. 
print(metin1[:6]) #baştan 6. karaktere kadar yazdır. 6. karakter dahil
print(metin3[0:16:2]) #0. indexten 8. indexe kadar 2 atlayarak karakterleri yazdrır. Dilimleme işlemi yapar.


#Veri Türlerini Dönüştürme
a='5'
b='10'

print(a+b)
print(int(a)+int(b))

a=int(a)
b=int(b)
print(a+b)



