#kullanıcının girdiği bir metni kullanıcının istediği kadar tekrar yazdıran fonksiyon

metin=input("Yazdırılacak metni giriniz")
tekrarsayisi=int(input("Tekrar sayısını giriniz"))

def yazdir(x,y):
    for i in range(1,y+1):
        print(x, end='\n')

yazdir(metin,tekrarsayisi)