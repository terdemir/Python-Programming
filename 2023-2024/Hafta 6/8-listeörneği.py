sehirler=[
    {"sehir":"amasya", "plaka":"05"},
    {"sehir":"çorum", "plaka":"19"},
    {"sehir":"samsun", "plaka":"55"},
    {"sehir":"tokat", "plaka":"60"}
]

for yer in sehirler:
    if(int(yer["plaka"])<20):
        print(yer["sehir"])

dersler=["Web Tasarımı", "Python Programlama", "Ağ temelleri", 
         "Çoklu Ortam", "İnternet Programcılığı", "Nesne Tabanlı Programlama"]

for ders in dersler:
    if "Program" in ders:
        print(ders)

notlar=[
    {"ders":"Web tasarımı","puan":"60"},
    {"ders":"Python","puan":"80"},
    {"ders":"Ağ","puan":"90"},
    {"ders":"Nesne","puan":"40"}
]

#Derslerden alınan puan ortalamasını buldurunuz.
