import random

sayi=random.randint(0,100)
print("0-100 arasında bir sayı tuttum, tahmin et!")
sayac=0

while True:
    sayac+=1
    cevap=int(input("0-100 araında bir sayı giriniz"))
    if(cevap>sayi):
        print("Daha küçük bir sayı giriniz.")
    elif(cevap<sayi):
        print("Daha büyük bir sayı giriniz.")
    else:
        print("Tebrikler sayıyı {}. denemede buldunuz.".format(sayac))
        break


