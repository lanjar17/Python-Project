# program hitung gaji pokok dan gaji bersih

KodeKaryawan = int(input('Masukkan kode karyawan : '))
NamaKaryawan = input('Masukkan nama karyawan : ')
Golongan = input('Masukan golongan : ')

print('====================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('-----------------------------------------------------------')

print('Nama Karyawan :' + NamaKaryawan + '(Kode Karyawan :' + str(KodeKaryawan) + ')') 
print('Golongan :' + Golongan)
print('-----------------------------------------------------------')

if(Golongan == 'A'):
    GajiPokok = 10000000
    Potongan = 2.5
    JumlahPotongan = 2.5 / 100 * 10000000
    GajiBersih = 10000000 - JumlahPotongan
elif(Golongan == 'B'):
    GajiPokok = 8500000
    Potongan = 2.0
    JumlahPotongan = 2.0 / 100 * 8500000
    GajiBersih = 8500000 - JumlahPotongan
elif(Golongan == 'C'):
    GajiPokok = 7000000
    Potongan = 1.5
    JumlahPotongan = 1.5 / 100 * 7000000
    GajiBersih = 7000000 - JumlahPotongan
elif(Golongan == 'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    JumlahPotongan = 1.0 / 100 * 5500000
    GajiBersih = 5500000 - JumlahPotongan
    
print('GajiPokok : Rp' + str(GajiPokok))
print('Potongan (' + str(Potongan) + '%): Rp' + str(JumlahPotongan))
print('-----------------------------------------------------------')
print('GajiBersih : Rp' + str(GajiBersih))
