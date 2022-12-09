def faktoriyel(sayi):
    sonuc=1
    if (sayi==1 or sayi==0):
        sonuc=1
    elif (sayi>1):
        for i in range(1, sayi+1,1):
            sonuc=sonuc*i
    else:
        print("0 veya daha büyük bir sayı giriniz")
    return sonuc


islem=faktoriyel(int(input("Sayı giriniz:")))
toplam=100+islem
print("Sonuç= ", toplam)
