a = [1, 5, 6, 3, 6, 9, 11, 20, 12, 4]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9, 8]
print('a = ', a)
print('b = ', b)

# menyisipkan nilai ke dalam indeks
print('\nSisipkan nilai 10 ke dalam indeks ke 3 dari a, dan 15 ke dalam indeks 2 dari b')
a.insert(3, 10)
b.insert(2, 15)
print('a = ', a)
print('b = ', b)

# menyisipkan nilai ke dalam indeks
print('\nSisipkan nila 4 ke indeks terakhir dari a, dan 8 ke indeks terakhir dari b')
a.append(4)
b.append(8)
print('a = ', a)
print('b = ', b)

# melakukan sorting
print('\nKemudian lakukan sorting secara ascending pada list a dan b')
a.sort()
b.sort()
print('a = ', a)
print('b = ', b)

# membuat sublist
print('\nBuatlah list c yang elemennya merupakan sublist dari a (mulai dari indeks ke 0 s/d 7), dan list d yang elemennya merupakan sublist dari b (mulai indeks ke 2 s/d 9)')
c = a[:8]
d = b[2:10]
print('c = ', c)
print('d = ', d)

# mendapatkan list dengan penjumlahan
print('\nLangkah untuk mendapatkan list e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya')
e = []
n = 0
for n in range (len(c)):
    indeks = c[n] + d[n]
    e = e + [indeks]
print('e = ', e)

# mengubah ke bentuk tuple
print('\nUbahlah list ke dalam bentuk tuple')
Tuple = tuple(e)
print('e = ', Tuple)

# mencari nilai min, maks, dan jumlah
print('\n')
minimal = min(Tuple)
maksimal = max(Tuple)
jmlh = sum(Tuple)
print('Nilai minimal : ', minimal)
print('Nilai maksimal : ', maksimal)
print('Jumlah seluruh elemen e : ', jmlh)

# membuat string
print('\n')
myString = "python adalah bahasa pemrograman yang menyenangkan"
print(myString)

# menentukan penyusun huruf
print('\n')
penyusun = set(myString)
print('Karakter huruf yang menyusun string tersebut adalah : ', penyusun)

# mengurutkan secara alfabet
print('\n')
List = list(penyusun)
print('himpunan karakter huruf yang diperoleh : ', sorted(List))


