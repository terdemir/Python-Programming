def asalmi(sayi):
    sayac=2
    toplam=0
    while sayac<=int(sayi/2):
        if(sayi%sayac==0):
            toplam+=1
        sayac+=1
    
    if toplam==0:
        print("Sayı asal")
    else:
        print("Asal Değil")

deger=int(input("Kontrol edilecek sayıyı giriniz: "))
asalmi(deger)