parola=input("parolayı giriniz")
parolatekrar=input("parolayı tekrar giriniz")

if(parola==parolatekrar):
    if(len(parola)>=8):
        print("Parola kabul edildi")
    else:
        print("Parola istenen uzunlukta değil")
else:
    print("parolalar aynı değil")