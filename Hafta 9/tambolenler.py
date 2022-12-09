#kullanıcının girdiği sayının tam bölenlerini bulan fonk
def tambolenler(sayi):
    tambolenler=[]
    for i in range(2, sayi+1):
        if(sayi%i==0):
            tambolenler.append(i)
    return tambolenler

say=int(input("Sayı giriniz"))

tam=tambolenler(say)
print(tam)