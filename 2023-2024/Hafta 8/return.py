def toplama(a,b):
    return a+b
x=int(input("sayı giriniz"))
y=int(input("tekrar bir sayı giriniz"))
sonuc=toplama(x,y)
print(sonuc)


def cikarma():
    sayi1=int(input("1.sayıyı giriniz"))
    sayi2=int(input("2.sayıyı giriniz"))
    return sayi1-sayi2

sonuc2=cikarma()
print(sonuc2)

#hem parametresiz hem de parametreli olarak geri değer döndüren bir fonksiyon tanımlanabilir.
#Yukarıdaki toplama parametreli iken, çıkarma işlemi parametresiz olarak tanımlanmıştır. 