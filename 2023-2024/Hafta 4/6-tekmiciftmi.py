'''
kullanıcının girdiği sayının tek mi çift mi olduğunu buldurunuz.
'''

sayi=int(input("Bir sayı giriniz: "))
kalan=sayi%2

if(kalan==0):
    print("Sayı çifttir.")
else:
    print("Sayı tektir")
