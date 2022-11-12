#SORU1: a,e,i,o,i,u,ö elemanlarını harf isimli listeye kayıt ediniz. i ve p harflarinin sayısını gösteriniz. 
#SORU2: liste=[34,1,56,334,0,2,5,20] hem küçükten büyüğe hemde büyükten küçüğe ekrana yazdırınız. 
#SORU3: liste=[1,2,3,4,5,6,7] 2-4 arasındaki elamanları yazdır, ilk 3 elemanı yazdır, 4 ten sonraki elemanları yazdır.
#SORU4: isimler=["osman", "mehmet"] bu listeye kendi adınız ekleyin. 
# Bu listenin başına kendi adınızı ekleyin. Bu listeden 2 nolu indise sahip elemanı çıkarın. listenin eleman sayısını yazdırın

#Cevap1:
from traceback import print_tb


harf=["a","e","i","o","u","i","ö"]
print(harf.count("i"))
print(harf.count("p"))

#Cevap2:
liste=[34,1,56,334,0,2,5,20]
liste.sort()
print(liste)
liste.reverse()
print(liste)

#Cevap3:
liste=[1,2,3,4,5,6,7]
print(liste[2:4])
print(liste[:3])
print(liste[4:])

#Cevap4:
isimler=["osman", "mehmet"]
isimler.append("turgay")
print(isimler)
isimler.insert(0,"turgay")
print(isimler)
isimler.pop(2)
print(isimler)
print(len(isimler))

