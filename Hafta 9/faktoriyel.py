def faktoriyel(sayi):
    sonuc=1
    if (sayi==1 or sayi==0):
        print("Sonuç= ", sonuc)
    elif (sayi>1):
        for i in range(1, sayi+1,1):
            sonuc=sonuc*i
        print("Sonuç= ", sonuc)
    else:
        print("0 veya daha büyük bir sayı giriniz")


faktoriyel(int(input("Sayı giriniz:")))

