#kullanıcıdan alınan listedeki sayıların ortalamasını bulan fonk.
def ortalama(sayilar):
    toplam=0
    ortalama=0
    for i in range(len(sayilar)):
        toplam=toplam+sayilar[i]
    ortalama=toplam/len(sayilar)
    return ortalama

def sayial():
    adet=int(input("Kaç sayı gireceksiniz: "))
    sayilar=[]

    for i in range (adet):
        print(i+1, ". sayıyı giriniz: ")
        sayi=int(input())
        sayilar.append(sayi)
    return sayilar

sayilar=sayial()
sonuc=ortalama(sayilar)
print("Sonuç= ", sonuc)
    

    