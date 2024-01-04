vize=int(input("Vize notunuzu giriniz: "))
final=int(input("Final notunuzu giriniz: "))
ortalama=(vize*40/100)+(final*60/100)

if(ortalama>=60):
    print("Dersi geçtiniz")
else:
    print("Dersten kaldınız")

print("\nDeğerlendirme tamamlandı")