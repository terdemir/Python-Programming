from calendar import SATURDAY
import random

sayi=random.randint(0,100)
sayac=0
print("0-100 arasında bir sayı tuttum tahmin et!")
while True:
    sayac+=1
    cevap=int(input("0-100 arasında bir sayı giriniz"))
    if(cevap>sayi):
        print("Daha küçük sayı girmelisin")
    elif(cevap<sayi):
        print("Daha büyük sayı girmelisin")
    else:
        print("Tebrikler tuttuğum sayıyı bildin")
        break
print("Tebrikler {} seferde sayıyı buldun.".format(sayac))