ortalama=0
toplam=0
for i in range(1,6):
    sayi=int(input("{}. sayıyı giriniz: ". format(i)))
    toplam=toplam+sayi
ortalama=toplam/5
print(int(ortalama))
