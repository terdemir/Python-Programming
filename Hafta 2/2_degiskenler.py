sayi1=5
print("sayi1=", sayi1)
#sayi1 değişkenine 5 değeri atanır. Sayısal değişken olduğu anlaşılır.
sayi1=10
print("sayi1 değişkeni=",sayi1, "oldu")
sayi1='Turgay' #sayi1 string oldu
print("Sayi1=", sayi1, "oldu")
sayi1=10.5 #değişken türü float oldu
print("Sayi1=", sayi1, "oldu")


#Toplu değişken atama

adi, soyadi, yas= 'Turgay', 'Erdemir', 34
print("isim", adi)
print("Soyisim", soyadi)
print("Yaşı", yas)

a=b=c=5
print("A=", a)
print("B=", b)
print("C=", c)

#print(adi+a) metin ve sayısal iki değişken birleştirme hatası verir. 

'''print(meslek) şeklinde önceden tanımlanmayan bir değişken olursa \n
python is not defined hatası verir'''

#ilk değeri belli olmayan değişken kullanmak gerekirse

yenisayi=int() #bu durumda python 0 değerini atar
print(yenisayi)

########******Değişken Adlandırma Kuralları*******########
'''
1. Değişken isimleri küçük harf, büyük harf ya da _ ile başlamalıdır. 
2. Değişken isimleri özel karakterler ve rakamlar ile başlayamaz
3. Değişken adında küçük harf, büyük harf, rakam ve _ kullanabilir.
4. Değişken isimleri herhangi bir uzunlukta olabilir.
5. Türkçe karakter desteği vardır. Lakin kullanılmaması önerilir.
6. Python dilinde ayrılmış özel kelimeler vardır. Bunlar değişken ismi olarak kullanılamaz. 
Bunları görüntülemek için:
import keyword
keyword.kwlist

(false, true, not, None, del, elif, def, for, and, or, while, else, if, .....)

7. büyük küçük harf duyarlılığı vardır'''

sayi=5
print(sayi)


