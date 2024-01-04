'''kullanıcının girdiği iki aralıktaki tek sayıları bulup ekrana yazdıran py kodu'''

ilk=int(input("İlk sayıyı giriniz"))
son=int(input("Son sayıyı giriniz"))

if(ilk<son):
    while ilk<=son:
        if(ilk%2==1):
            print(ilk)
        ilk+=1