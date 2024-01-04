takimlar=["GS","Bjk","Ts"]

#append: liste sonuna eleman ekler.
takimlar.append("fb")
print(takimlar)

#insert: listede istenen araya eleman ekler.
takimlar.insert(2,"Bşk")
print(takimlar)

#copy: listeyi kopyalar.
takimlar2=[]
takimlar2=takimlar.copy()
print(takimlar2)

#count: bir elemanın listede kaç defa olduğunu sayar.
print(takimlar.count("fb"))

#extend: bir listeye başka bir listenin elemanlarını ekler.
takimlar3=["sivas", "adana"]
takimlar.extend(takimlar3)
print(takimlar)

#clear: listeyi temizler, elemanları siler.
takimlar2.clear()
print(takimlar2)

#pop: bir elemanı (index no ile) listeden siler.
takimlar.pop(4)
print(takimlar)

#remove: istenen  elemanı listeden çıkarır.
takimlar.remove("Bşk")
print(takimlar)

#reverse: listeyi ters çevir
takimlar.reverse()
print(takimlar)

#sort: listeyi sıralar.
takimlar.sort()
print(takimlar)

#del: index numarasını göre silme.
del takimlar[2]
print(takimlar)

#len: listenin uzunluk bilgisini (eleman sayısını) verir.
print(len(takimlar))