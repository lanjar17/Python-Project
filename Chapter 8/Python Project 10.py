def buy(beli, kg):
    harga = buah.get(beli)
    total = harga * kg
    return total

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('Silahkan dipilih : ')
for i in buah.keys():
    print('{0}'.format(i))


total = 0
selesai = False
while not selesai:
    
    while True:
        namaBuah = str(input('\nNama buah yang dibeli : '))
        if namaBuah not in buah.keys():
            print('Buah tidak ada')
            continue
        else:
            break
    while True:
        try:
            banyak = float(input('Berapa Kg             : '))
        except ValueError:
            print('Input angka saja !')
            continue
        else:
            break

    total = total + buy(namaBuah, banyak)
    jawab = None
    while jawab not in ("y", "n"):
        jawab = str(input('\nBeli buah lagi (y/n)? : '))
        if jawab == "y":
          selesai = False
          print('')
        
        elif jawab == "n":
            selesai = True
print('-----------------------------------')
print('Total harga           : Rp {0}'.format(buy(namaBuah, banyak)))
    

