#vize, final puanları ve yüzdelik oranlarını parametre olarak alan 
# ve puanlar ile yüzdelik oranları çarparak ortalamayı döndüren fonksiyonu yazınız.

def hesapla(vize, final, vizeyuzde, finalyuzde):
    ortalama=(vize*vizeyuzde/100)+(final*finalyuzde/100)
    return ortalama


vpuan=int(input("Vize puanı giriniz"))
vyuzde=int(input("Vize yüzdesini giriniz"))
fpuan=int(input("Final puanı giriniz"))
fyuzde=int(input("Final yüzdesini giriniz"))

sonuc=hesapla(vpuan, fpuan, vyuzde, fyuzde)
print(sonuc)