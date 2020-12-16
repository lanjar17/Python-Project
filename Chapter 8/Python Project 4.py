dataSayur = ['bayam', 'kangkung', 'wortel', 'selada']
def myData(x):
    print('Data sayur : ')
    for n in x:
        print('{0}'.format(n))
    print('')

while True:
    print('Menu: ')
    print('A. Tambah data sayur')
    print('B. Hapus data sayur')
    print('C. Tampilkan data sayur')
    jawab = None
    while jawab not in('A', 'B', 'C', 'D'):
        jawab = str(input('\nPilihan Anda: '))
        if(jawab == "A"):
            myData(dataSayur)
            tambah = str(input('Nama sayur yang akan ditambahkan : '))
            if tambah in dataSayur:
                print('Nama sayur sudah ada dalam data')
            else:
                dataSayur.append(tambah)
                print('{0} ditambahkan'.format(tambah))
                print('')
                myData(dataSayur)

        elif(jawab == "B"):
            myData(dataSayur)
            hapus = str(input('Nama sayur yang akan dihapus : '))
            if hapus in dataSayur:
                dataSayur.remove(hapus)
                print('{0} dihapus'.format(hapus))
                print('')
                myData(dataSayur)
            else:
                print('Sayur tidak ditemukan')

        elif(jawab == "C"):
            print(dataSayur)

        elif(jawab == "stop"):
            exit()

        else:
            print('Masukan pilihan')
            
            
                
