# print konsola çıktı gönderme fonksiyonudur
print("Merhaba")
print('Python')

# print('Türkiye'nin başkenti Ankara'dır') hata verir. 
print("Türkiye'nin başkenti Ankara'dır")

#print fonksiyonu parametreleri \ Kaçış Parametreleri
print('Bursa\'nın iskenderi meşhurdur') # \ kendinden sonra gelen karakterin özel görevini iptal eder.

print("Satır1\nSatır2\nSatır3") # \n alt satıra geçme işlemi yapar

print("Pazartesi\t Salı\t Çarşamba") # \t metinler arasında bir tab boşluk bırakır.

print ("Pazartesi", "Salı", "Çarşamba", sep="_") # sep yazılanlar arasında belirlenen işareti ekler.

#Format Parametresi
a=5
b=6
c=7
print(a,b,c, " sayılarının toplamı=", a+b+c, " dir")
print("{},{},{} sayılarının toplamı= {}'dir".format(a,b,c,a+b+c))

not1=70
not2=100

print("1. Sınav notu={}\n2. Sınav notu={}\nOrtalama={}".format(not1, not2, (not1+not2)/2))








