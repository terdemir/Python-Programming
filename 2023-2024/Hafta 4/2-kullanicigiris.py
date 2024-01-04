'''
Kullanıcıdan alınan kullanıcı adının "merzifon" ve parolanın "Myo05" olması durumunda 
"Kullanıcı girişi başarılı" aksi halde "Bilgiler hatalı" uyarısı veren kod parçacığını yazınız.
'''

kadi=input("Kullanıcı adınız giriniz")
parola=input("Parolayı giriniz")

if(kadi=="merzifon" and parola=="Myo05"):
    print("Kullanıcı girişi başarılı")
else:
    print("Giriş başarısız")
    