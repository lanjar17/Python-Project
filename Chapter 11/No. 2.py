from datetime import *

def book(kode, nama, judul):
    file = open(myFile, "a")
    time = datetime.date(datetime.now())
    timeBack = time + timedelta(days=7)
    data = [kode, nama, judul, str(time), str(timeBack)]
    file.write('|'.join(data) + "\n")
    file.close

myFile = "dataPinjaman.txt"
while True:
    kode = str(input("\nMasukan Kode Member\t: "))
    nama = str(input("Masukan Nama Member\t: "))
    judul = str(input("Masukan Judul Buku\t: "))
    book(kode, nama, judul)
    jawab = None
    while jawab not in ("y", "n"):
        jawab = str(input("\nUlangi lagi (y/n)\t: "))
        if jawab == "y":
            continue
        elif jawab == "n":
            exit()
        else:
            print("Masukan Pilihan (y/n)")
