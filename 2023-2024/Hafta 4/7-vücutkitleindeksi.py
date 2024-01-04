'''
Vücut kitle indeksi bireyin ağırlığının boyunun karesine bölümü ile hesaplanır.
indeks 18 ve altında ise zayıf, 
25 ve  altında arasında ise normal,
30 ve altında ise kilolu,
daha fazla ise obez 

ekrana durumunu ve indeksini yazdırınız.

ÖRNEK: "Vücut kitle indeksi normal, değeri=20"

Bir kullanıcıdan boy ve ağırlık bilgisi alarak vücut kitle indeksini hesaplayınız. 
'''
boy=int(input("Boyunuzu giriniz (cm): "))
kilo=int(input("Kilonuzu giriniz (kg): "))

boy=boy/100
indeks=kilo/boy**2

if(indeks<=18):
    print("Vücut kitle indeksi zayıf, değeri=", indeks)
elif(indeks<=25):
    print("Vücut kitle indeksi normal, değeri=", indeks)
elif(indeks<=30):
    print("Vücut kitle indeksi kilolu, değeri=", indeks)
else:
    print("Vücut kitle indeksi obez, değeri=", indeks)