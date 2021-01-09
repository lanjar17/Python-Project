def getGapok(gol):
    gaji = 0
    if gol == 'A':
        gaji = 'Rp 4000000'
    elif gol == 'B':
        gaji = 'Rp 4500000'
    elif gol == 'C':
        gaji = 'Rp 5000000'
    else:
        print('Golongan Tidak Sesuai')
    return gaji
    

myFile = "dataKaryawan.dat"
file = open(myFile, "r")
data = file.read()
data = data.replace("\n", "|")
data = data.split("|")
data.remove('')
dataKaryawan = {}
n = 0
for x in range(len(data)//6):
    dataKaryawan[data[n]] = (data[n+1], data[n+2], data[n+3], data[n+4], data[n+5])
    n += 6
file.close()

while True:
    try:
        kode = str(input('Masukkan Kode Karyawan : '))
        data = dataKaryawan.get(kode)
        data = list(data)
        print('\nKode Karyawan\t: ', kode)
        print('Nama Karyawan\t: ', data[0])
        print('Alamat\t        : ', data[1])
        print('Golongan\t: ', data[2])
        print('Gaji Pokok\t: ', getGapok(data[2]))
        print('Tanggal Lahir\t: ', data[3], '(Usia: ', data[4], 'Tahun)')
        break
    except:
        print('Data Tidak Ditemukan' + '\n')