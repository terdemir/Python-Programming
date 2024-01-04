'''
Soru 1: Kullanıcının girdiği iki sayı arasındaki çift sayıların ortalamasını fonksiyon ile buldurunuz.
Soru 2: Ana programda vize, final puanları ve vize ile finalin yüzdelik oranlarını kullanıcıdan alarak 
parametre olarak kullanarak ortalamayı geri döndüren fonksiyonu yazınız. 
'''

#Cevap 1: 
def ciftortalama(x,y):
    toplam=0
    ortalama=0
    sayac=0
    for i in range (x,y+1,1):
        if(i%2==0):
            toplam=toplam+i
            sayac=sayac+1
    ortalama=toplam/sayac
    return ortalama

s1=int(input("başlangıç sayısını giriniz"))
s2=int(input("Bitiş sayısını giriniz"))
sonuc=ciftortalama(s1,s2)
print(sonuc)

#Cevap 2:
vpuan=int(input("Vize notunu giriniz"))
vyuzde=int(input("Vize yüzdesini giriniz"))
fpuan=int(input("Final notunu giriniz"))
fyuzde=int(input("Final yüzdesini giriniz"))

def hesapla(v,f,vy,fy):
    ortalama=(v*vy/100)+(f*fy/100)
    return ortalama

sonuc2=hesapla(vpuan,fpuan,vyuzde,fyuzde)
print(sonuc2)

