metin=input('Bir cümle yazınız:')
harf=input('Sayısı istenen harfi giriniz:')
sayac=0
for i in metin:
    if i==harf:
        sayac=sayac+1
print("Cümle içerisinde geçen "+ harf+ " harfi sayısı=", sayac)


sesliharf='aeıioöuü'
sayac=0
for i in metin:
    if i in sesliharf:
        sayac=sayac+1
print("Cümle içerisinde geçen sesli harfi sayısı=", sayac)

sesliler=""

for i in metin:
    if i in sesliharf:
        sesliler=sesliler+i
print("sesli harfler: ", sesliler)
