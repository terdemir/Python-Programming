def asalmi(sayi):
    sayac=2
    toplam=0
    while sayac<=int(sayi/2):
        if sayi%sayac==0:
            toplam+=1
        sayac+=1
    if toplam==0:
        print("Asal")
    else: 
        print("Değil")


deger=int(input("Sayıyı girin"))
asalmi(deger)
