def yazdir(metin,tekrar):
    for i in range(1, tekrar+1):
        print(metin, end='\n')


yazi=input("Yazdırılacak metni giriniz")
tekrarsayisi=int(input("Tekrar sayısını giriniz"))
yazdir(yazi,tekrarsayisi)