'''in işleci: bir liste ya da karakter içerisinde bir değerin olup olmadığını kontrol eder. '''

"p" in 'python'
'a' in 'python'

isim='Turgay'
for i in isim:
    print(i, end=",")


i=0
while i<len(isim):
    print(isim[i], end=',')
    i+=1
