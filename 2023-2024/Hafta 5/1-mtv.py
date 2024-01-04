'''
kullanıcı tarafından girilen araç

otomobil ise: 1-3 yaşında ise 1000, 4-7 yaşında ise 800, 7 den büyükse 500
motorsiklet ise: 1-3 yaşında ise 500, 4-7 yaşında ise 400, 7 den büyükse 300

girilen araç bilgilerine göre ne kadar mtv ödeneceğini belirleyen pyhton kodlarını yazınız.
'''

tur=int(input("Araç türünü giriniz: 1- Motorsiklet 2- Otomobil"))
yas=int(input("Araç yaşını giriniz: "))

if (tur==1):
    if(yas>=1 and yas<=3):
        print("MTV=500TL")
    elif(yas>=4 and yas<=7):
        print("MTV=400TL")
    elif(yas>7):
        print("MTV=300TL")

if (tur==2):
    if(yas>=1 and yas<=3):
        print("MTV=1000TL")
    elif(yas>=4 and yas<=7):
        print("MTV=800TL")
    elif(yas>7):
        print("MTV=500TL")