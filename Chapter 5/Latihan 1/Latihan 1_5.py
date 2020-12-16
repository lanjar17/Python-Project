# program hitung gaji pokok dan gaji bersih

KodeKaryawan = int(input('Masukkan kode karyawan : '))
NamaKaryawan = input('Masukkan nama karyawan : ')
Golongan = input('Masukan golongan : ')
Status = input('Masukan status (1: menikah,2: blm) : ')
if(Status == '1'):
    JumlahAnak = int(input('Masukan jumlah anak : '))
    TunjanganMenikah = 10 / 100
    TunjanganAnak = 5 / 100 * JumlahAnak
    StatusMenikah = 'Sudah Menikah'
else:
    JumlahAnak = 0
    TunjanganMenikah = 0
    TunjanganAnak = 0
    StatusMenikah = 'Belum Menikah'

print('====================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('-----------------------------------------------------------')

print('Nama Karyawan :' + NamaKaryawan + '(Kode Karyawan :' + str(KodeKaryawan) + ')') 
print('Golongan :' + Golongan)
print('Status Menikah :' + StatusMenikah)
print('Jumlah Anak :' + str(JumlahAnak))
print('-----------------------------------------------------------')

if(Golongan == 'A'):
    GajiPokok = 10000000
    Potongan = 2.5
    JumlahTunjanganMenikah = 10000000 * TunjanganMenikah
    JumlahTunjanganAnak = 10000000 * TunjanganAnak
    GajiKotor = GajiPokok + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 2.5 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
elif(Golongan == 'B'):
    GajiPokok = 8500000
    Potongan = 2.0
    JumlahTunjanganMenikah = 8500000 * TunjanganMenikah
    JumlahTunjanganAnak = 8500000 * TunjanganAnak
    GajiKotor = GajiPokok + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 2.0 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
elif(Golongan == 'C'):
    GajiPokok = 7000000
    Potongan = 1.5
    JumlahTunjanganMenikah = 7000000 * TunjanganMenikah
    JumlahTunjanganAnak = 7000000 * TunjanganAnak
    GajiKotor = GajiPokok + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 1.5 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
elif(Golongan == 'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    JumlahTunjanganMenikah = 5500000 * TunjanganMenikah
    JumlahTunjanganAnak = 5500000 * TunjanganAnak
    GajiKotor = GajiPokok + JumlahTunjanganMenikah + JumlahTunjanganAnak
    JumlahPotongan = 1.0 / 100 * GajiKotor
    GajiBersih = GajiKotor - JumlahPotongan
print('GajiP okok : Rp' + str(GajiPokok))
print('Tunjangan Suami/Istri : Rp' + str(JumlahTunjanganMenikah))
print('Tunjangan Anak : Rp' + str(JumlahTunjanganAnak))
print('-----------------------------------------------------------')
    
print('Gaji Kotor : Rp' + str(GajiKotor))
print('Potongan (' + str(Potongan) + '%): Rp' + str(JumlahPotongan))
print('-----------------------------------------------------------')
print('GajiBersih : Rp' + str(GajiBersih))
