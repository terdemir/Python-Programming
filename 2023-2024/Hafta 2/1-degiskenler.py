sayi1=5
#sayi1 değişkenine 5 değeri atandı. Sayısal değişken olarak tanımlandı

print ("Sayı1=", sayi1)

sayi1=10
print("Sayı1 değişkeni=", sayi1, " oldu") #sayi1 değişkeni değiştirildi

sayi1='Turgay'
print("Sayı1 değişkeni=", sayi1, " oldu") #sayi1 değişkeninin türü değiştirildi ve string yapıldı

sayi1=10.5
print("Sayı1 değişkeni=", sayi1, " oldu") #sayi1 değişkeninin türü float oldu.

#Toplu Değişken Atama
adi, soyadi, yas="Turgay","Erdemir",35
print("İsim :", adi)
print("Soyisim :", soyadi)
print("Yaşı :", yas)

a=b=c=5

print("A= ", a)
print("B= ", b)
print("C= ", c)


isim="Turgay"

#print(sayi1+isim) metin ve sayısal değişken türü farklı olduğu için hata verecektir.

'''print(meslek) şeklinde önceden tanımlanmamış bir değişken olursa \n python is not defined hatası verecektir.'''

#ilk değeri belli olmayan değişken kullanmak gerekirse

yenisayi=int() #değer olarak 0 atanır
print(yenisayi)

tur=type(yenisayi)
print(tur)
print(type(isim))

##############Değişken İsimlendirme Kuralları###################
'''
1. Değişken isimleri küçük harf, büyük harf ya da _ ile başlamalıdır.
2. Değişken isimleri özel karakterler ve rakamlar ile başlayamaz.
3. Değişken adında küçük harf, büyük harf ve rakamlar kullanılabilir.
4. Değişken isimleri herhangi bir uzunlukta olabilir.
5. Türkçe karakter desteği vardır. Lakin kullanılmaması önerilir.
6. Python dilinde ayrılmış özel kelimeler vardır. Bunlar değişken ismi ol olarak kullanılamaz.
Bunları görüntülemek için: 
import keyword
keyword.kwlist

Örnekler: (false, true, not, None, del, elif, def, for, and, or, while, else, if ....)

7. Büyük küçük harf duyarlılığı vardır.

'''

import keyword
keyword.kwlist

sayi2=10
Sayi2=20
print(sayi2)
print(Sayi2)