namaFile = input('Masukan nama file : ')
try:
    file = open(namaFile, "r")
    print('Isi file', namaFile, 'adalah : ')
    print(file.read())

except FileNotFoundError:
    print('File tidak ditemukan')
