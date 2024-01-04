''' kullanıcının girdiği iki sayı arasındaki sayıların toplamını buldurunuz.'''

sayi1=int(input("1. sayıyı giriniz"))
sayi2=int(input("2. sayıyı giriniz"))

toplam=0
for i in range(sayi1, sayi2):
    toplam+=i
print(toplam)

toplam2=0
for i in range(sayi1,sayi2):
    if i%2==0:
        toplam2+=i
print(toplam2)