'''
Kullanıcıdan alınan 2 sayıdan 1. sayı 2. sayıya tam bölünüyor is ekrana "Tam bölünüyor" yazdıran, 
aksi durumda "kalan= ..." ile kalan sayıyı gösteren program 
'''

sayi1=int(input("1. sayıyı giriniz: "))
sayi2=int(input("2. sayıyı giriniz: "))

kalan=sayi1%sayi2

if(kalan==0):
    print("Tam bölümüyor")
else:
    print("Kalan=", kalan)
