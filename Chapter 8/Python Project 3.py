import random
while True:
    try:
        n = int(input('Input jumlah Mahasiswa yang ingin dimasukkan : '))
        break
    except:
        print('Bukan jumlah nama mahasiswa')
print('Silahkan input {0} mahasiswa'.format(n))

nama = []
while n > 0:
    try:
        mhs = str(input('Masukan nama Mahasiswa : '))  
    except:
        print('Bukan nama Mahasiswa')
        continue
    nama = nama + [mhs]
    n -= 1
nama.sort()
print('-'*30)
print('Susunan nama Mahasiswa')
for x in nama:
    print('{0} ({1} karakter)'.format(x, len(x)))
    


                  
