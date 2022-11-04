'''range işlevi istenen aralıkta sayı dizisi oluşturur.'''

print(*range(10))

print(*range(5,30))

print(*range(1,20,3))

toplam=0
for i in range(20):
    toplam=toplam+i
print(toplam)    

for i in range(20,0,-1):
    print(i)

