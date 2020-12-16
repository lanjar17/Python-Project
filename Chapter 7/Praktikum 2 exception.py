# solusi mengatasi exception

try:
    file = open("c:/data.txt", "r")
    bil1 = int(file.readline())
    bil2 = int(file.readline())
    hasil = bil1/bil2
    print(bil1, 'dibagi', bil2, 'sama dengan', hasil)

except FileNotFoundError:
    print('File tidak ditemukan')
except ZeroDivisionError:
    print('Tidak boleh pembagian dengan nol')
