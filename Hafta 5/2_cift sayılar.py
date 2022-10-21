sayac=1
toplam=0
while sayac<=100:
    if sayac%2==0:
        print(sayac, end=",")
    toplam=toplam+sayac
    sayac+=1
print("\nToplam=",toplam)