takimlar=['GS','Bjk', 'Ts']
#append : listeye eleman ekler
takimlar.append("fb")
print(takimlar)

#insert: listede istenen araya elaman yerleştirir
takimlar.insert(2,'Ss')
print(takimlar)

#copy: listeyi kopyalamaya yarar
takimlar2=[]
takimlar2=takimlar.copy()
print(takimlar2)

#count: bir elemanın listede kaç defa olduğunu sayar
print(takimlar.count('fb'))

#extend: bir listeye başka bir listenin elemanlarını ekler
takimlar.extend(takimlar2)
print(takimlar)

#clear: listeyi temizler, elemanları siler
takimlar2.clear()
print(takimlar2)

#pop: bir elemanı(indis no ile) listeden siler
takimlar.pop(4)
print(takimlar)

#remove: istenen elemanı listeden çıkarır
takimlar.remove("fb")
print(takimlar)

#reverse: listeyi tersten yazdırır
takimlar.reverse()
print(takimlar)

#sort: listeyi alafabetik sıralar
takimlar.sort()
print(takimlar)

#del: indis numarasına göre silme
del takimlar[2]
print(takimlar)

#len: listenin uzunluk bilgisini (eleman sayısı) verir.
print(len(takimlar))

