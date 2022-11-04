puan=0
toplam=0
for i in range(1,11):
    puan=int(input("{}. notu giriniz" .format(i)))
    toplam=toplam+puan
ortalama=toplam/10
print("Ortalama= ", ortalama)
