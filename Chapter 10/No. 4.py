myfile = open("dataMhs.txt", "r")
data = myfile.readlines()
i = 0
new = []
for lists in data:
    dataMhs = str(data[i])
    dataMhs = dataMhs.split('|')
    new.append(dataMhs)
    i += 1

cari = input('Masukkan NIM yang mau dicari : ')
hasil = False
a = 0
for x in new:
    if cari in new[a]:
        b = 0
        for lists in new:
            if cari == new[b][0]:
                print('Data Mahasiswa')
                print('NIM\t : '+ new[b][0])
                print('Nama\t : '+ new[b][1])
                print('Alamat\t : '+ new[b][2])
                hasil = True
                break
            else:
                b += 1
    a += 1

if hasil == False :
    print('Data mahasiswa tidak ditemukan')
