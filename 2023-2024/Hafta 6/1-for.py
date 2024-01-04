"p" in "python"
"a" in "python"

#in işlemi: bir liste ya da bir metin içinde bir değerin olup olmadığını kontrol eder.

isim="Turgay"

for i in isim:
    print(i, end=", ")

i=0
while i<len(isim):
    print(isim[i], end=", ")
    i+=1
