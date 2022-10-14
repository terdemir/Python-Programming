print("VÜCUT KİTLE ENDEKSİ HESAPLAMA PROGRAMI")
boy=float(input("Boyunuzu giriniz(cm):"))
kilo=float(input("Kilonuzu giriniz(kg):"))
boy=boy/100
endeks=kilo/(boy*boy)
if(endeks<=18):
    print("\n Zayıf:{}" .format(endeks))
elif(endeks>18 and endeks<=25):
    print("\n Normal:{}" .format(endeks))
elif(endeks>25 and endeks<=30):
    print("\n Kilolu:{}" .format(endeks))
else:
    print("\n Obez:{}" .format(endeks))
