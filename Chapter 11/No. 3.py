from datetime import *
from datetime import date

def diffDate(x):
    skrg = datetime.date(datetime.now())
    x = x.split('-')
    x = date(int(x[0]), int(x[1]), int(x[2]))
    selisih = (x - skrg).days
    return selisih

def seacrh(kode):
    file = open(myFile, "r")
    myfile = file.read().splitlines()
    for i in myfile:
        data = i.split("|")
        if kode == data[0]:
            print('\nData Peminjaman Buku')
            print('Kode Member\t        :', data[0])
            print('Nama Member\t        :', data[1])
            print('Judul Buku\t        :', data[2])
            print('Tanggal Mulai Pinjaman\t:', data[3])
            print('Tanggal Maks Pinjaman\t:', data[4])
            print('Tanggal Pengembalian\t:', datetime.date(datetime.now()))

            terlambat = diffDate(data[4])
            if terlambat < 0:
                back = terlambat * (-1)
                print('Terlambat\t        : {} hari'.format(back))
                denda = 2000 * abs(back)
                print('Denda\t                : Rp {} '.format(denda))
            elif terlambat > 0:
                print('Terlambat\t        : Tidak Terlambat')
                
myFile = "dataPinjaman.txt"
kode = input('Masukan Kode Member\t: ')
seacrh(kode)
