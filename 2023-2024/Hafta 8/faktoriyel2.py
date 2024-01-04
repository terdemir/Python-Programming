#recursive fonksiyon: fonksiyon içinde kendisini çağırarak çalıştırılabilir fonksiyondur.
def faktoriyel(sayi):
    if sayi==1:
        return sayi
    else:
        return sayi*faktoriyel(sayi-1)
    
deger=int(input("Sayıyı giriniz"))
sonuc=faktoriyel(deger)
print(sonuc)