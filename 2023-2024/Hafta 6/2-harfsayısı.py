''' kullanıcının girdiği bir kelime ya da cümlede 
yine kullanıcının girdiği bir harfin kaç defa tekrar ettiğini buldurunuz.'''

metin=input("Bir cümle/kelime yazınız: ")
harf=input("Sayısı istenen harfi giriniz: ")

sayac=0
for i in metin:
    if i==harf:
        sayac=sayac+1
print("Cümle/kelime içinde geçen" + harf +" harfi sayısı= ", sayac)

''' yukarıda girilen metnin içindeki sesli harf sayısını buldurunuz'''

sesliharf="aeıioöuü"
sayac2=0
for i in metin:
    if i in sesliharf:
        sayac2+=1
print("Cümle içindeki sesli harf sayısı= ", sayac2)


