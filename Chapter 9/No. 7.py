mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('='*63)
print('NIM'.ljust(10, ' '), 'NAMA MAHASISWA'.ljust(20, ' '), 'TGL LAHIR'.ljust(15, ' '), 'TEMPAT LAHIR'.ljust(20, ' '))
print('-'*63)

for data in mhs:
    dataList = data.split(':')
    lahir = dataList[2].split('-')
    tglLahir = lahir[2] + '/' + lahir[1] + '/' + lahir[0]
    print(dataList[0].ljust(10, ' '), dataList[1].ljust(20, ' '), tglLahir.ljust(15, ' '), dataList[3].ljust(20, ' '))

print('-'*63)
