namaFile = input('Masukan nama file : ')
try:
    while True:
        file = open(namaFile, "a")
        data = input('Data yang mau ditambahkan : ')
        file.write(data + "\n")
        file.close()
        print('Ulangi lagi (y/n)? : ')
        jawab = input()
        if jawab == 'n':
            break

    file = open(namaFile, "r")
    print('Isi file', namaFile, 'setelah ditambahkan adalah : ')
    print(file.read())

except FileNotFoundError:
    print('File tidak ditemukan')
