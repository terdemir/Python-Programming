ilk=int(input("Başlangıç değerini giriniz"))
son=int(input("Başlangıç değerini giriniz"))

while ilk<=son:
    if(ilk%2==1):
        print(ilk, end=",")
    ilk+=1
