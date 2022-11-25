def faktoriyel(sayi):
    sonuc=1
    if(sayi==0 or sayi==1):
        print("Sonuç=", sonuc)
    elif sayi>=1:
        for i in range(1, sayi+1, 1):
            sonuc*=i
        print("Sonuç=", sonuc)
    else:
        print("0 veya da daha büyük sayı girmelisiniz")


deger=int(input("Sayıyı girin"))
faktoriyel(deger)
