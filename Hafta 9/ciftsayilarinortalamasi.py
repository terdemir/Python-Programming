#kullanıcının girdiği iki sayı arasındaki çift sayıların ortalamasını bulan fonk?

def ciftortalama(sayi1,sayi2):
    toplam=0
    ortalama=0
    sayac=0
    for i in range(sayi1, sayi2+1, 1):
        if(i%2==0):
            toplam=toplam+i
            sayac+=1
        ortalama=toplam/sayac
    return ortalama


s1=int(input("başlangıç sayısını giriniz: "))
s2=int(input("bitiş sayısını giriniz: "))

sonuc=ciftortalama(s1,s2)
print(sonuc)