#bir fonksiyon başka bir fonksiyon içinde çağırılarak kullanılabilir. 
def yasHesapla(dogumyili):
    return 2023-dogumyili

def emeklilik(dogumyili):
    yas=yasHesapla(dogumyili)
    emeklilik=65-yas
    print("Emekliliğinize ", emeklilik, " yıl kalmıştır.")


dogum=int(input("Doğum yılınızı giriniz: "))
emeklilik(dogum)