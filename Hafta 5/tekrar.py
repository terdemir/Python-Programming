sayi1=int(input("1. sayıyı giriniz"))
sayi2=int(input("1. sayıyı giriniz"))
sayi3=int(input("1. sayıyı giriniz"))
enb=sayi1
if(sayi1<sayi2):
    enb=sayi2
    if(sayi2<sayi3):
        enb=sayi3
    
print("en büyük sayı=", enb)