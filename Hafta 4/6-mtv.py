#otomobilse 1-3 yaşında ise 1000, 4-7 yaşında ise 800, 7 den büyükse 500
#motorsiklet ise 1-3 yaşında ise 500, 4-7 yaşında ise 400, 7 den büyükse 300

tur=input("Araç türünü giriniz (Otomobil/Motorsiklet):")
yas=int(input("Araç yaşını giriniz:"))

if(tur=="Otomobil"):
    if(yas>=1 and yas<=3):
        print("vergi 1000TL")
    elif(yas>=4 and yas<=7):
        print("vergi 800TL")
    elif(yas>7):
        print("vergi 500TL")
if(tur=="Motorsiklet"):
    if(yas>=1 and yas<=3):
        print("vergi 500TL")
    elif(yas>=4 and yas<=7):
        print("vergi 400TL")
    elif(yas>7):
        print("vergi 300TL")