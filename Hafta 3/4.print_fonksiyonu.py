#print konsola çıktı gönderme fonksiyonu
print("Merhaba")
print('Python')

#print('Türkiye'nin başkenti Ankara'dır.') hata verecektir.
print("Türkiye'nin başkenti Ankara'dır.")

#Print Fonksiyonu ile Kullanılan Parametreler /Kaçış parametreleri
print('Bursa\'nın iskenderi meşhurdur') #\ kendinden sonra gelen karakterin özel görevini iptal eder.

print(" Satır1\n Satır2\n Satır3") #\n alt satıra geçme işlemi yapar

print("pazartesi\t salı\t çarşamba") #\t metinler arasında bir tab boşluk bırakır. 

print("pazartesi", "salı", "çarşamba", sep="_") # sep yazılanlar arasında belirlenen işareti ekler.

#Format Parametresi
a=2
b=4
c=6
print(a, b, c, " sayılarının toplamı", a+b+c, "dir")
print("{} {} {} sayılarının toplamı {} dir".format(a,b,c,a+b+c))

#Print Fonksiyonu Örnekler
#1.
print("Memleket isterim, \nGök mavi, dal yeşil, tarla sarı olsun,")
print("Memleket isterim,","Gök mavi, dal yeşil, tarla sarı olsun,")
print("Memleket isterim,")
print("Gök mavi, dal yeşil", "tarla sarı olsun,")
print("Memleket", "isterim", "Gök mavi", "dal", "yeşil", sep="-")

not1=55
not2=100
print('1.sınav notu:{} \n2.sınav notu:{}'.format(not1, not2))
