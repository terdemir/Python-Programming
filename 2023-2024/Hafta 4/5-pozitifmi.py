'''
Kullanıcının girdiği sayının pozitif mi, negatif mi, sıfır mı olduğunu buldurunuz.
'''

sayi=int(input("Bir sayı giriniz: "))

if(sayi>0):
    print("Sayı pozitiftir.")
elif(sayi<0):
    print("Sayı negatiftir.")
else:
    print("Sayı 0'dır.")