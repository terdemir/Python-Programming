''' range işlevi istenen aralıkta sayı dizisi oluşturur'''

print(*range(10))

print(*range(1,11))

print(*range(5,30))

print(*range(1,20,3))

toplam=0
for i in range(1,11):
    toplam=toplam+i
print(toplam)

print(*range(30,50,3))
print(*range(20,0,-1))


for i in range(100,50,-5):
    print(i)

