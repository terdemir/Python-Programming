#kullanıcının girdiği metni istediği sayıda ekrana yazdırır.

metin=input("Metin giriniz")
tekrar=int(input("Tekrar sayısını giriniz"))
for i in range(tekrar):
    print(metin)

#kullanıcının girdiği iki sayı arasındaki sayıların toplamını ekrana yazdıran program
sayi1=int(input("1. sayıyı giriniz"))
sayi2=int(input("2. sayıyı giriniz"))
toplam=0
for i in range(sayi1+1, sayi2):
    toplam=toplam+i
print(toplam)

