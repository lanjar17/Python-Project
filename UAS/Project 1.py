from datetime import *

def getUsia(tgl):
    skrg = datetime.date(datetime.now())
    x = tgl.split('-')
    x = date(int(x[0]), int(x[1]), int(x[2]))
    umur = (skrg - x).days
    umur = umur // 365
    return umur

def addKaryawan():
    nip = str(input('\nMasukkan NIP\t           : ').upper())
    nama = str(input('Masukkan Nama\t           : ').upper())
    alamat = str(input('Masukkan Alamat\t           : ').upper())
    gol = ("A") or ("B") or ("D")
    while True:
        gol = str(input('Masukkan Golongan\t   : '))
        if gol == ("A"):
            break
        elif gol == ("B"):
            break
        elif gol == ("C"):
            break
        else:
            print('Pilihan Golongan A, B, C')
    while True:
        try:
            tgl = input('Masukkan Tgl Lahir\t   : ')
            umur = str(getUsia(tgl))
            file = open(myFile, "a")
            hasil = [nip, nama, alamat, gol, tgl, umur]
            file.write('|'.join(hasil) + '\n' )
            file.close()
            break
        except ValueError:
            print('Format Tgl Lahir [YYYY-MM-DD]')
            
myFile = "DataKaryawan.dat"
addKaryawan()
jawab = None
while True:
    jawab = str(input('\nTambah data (y/n)?\t   : '))
    if jawab == "y":
        addKaryawan()
        continue
    elif jawab == "n":
        break
    else:
        print('Masukan pilihan (y/n)')
