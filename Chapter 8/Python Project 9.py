def buy(beli, kg):
    harga = buah.get(beli)
    total = harga * kg
    return total

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('Silahkan dipilih : ')
for i in buah.keys():
    print('{0}'.format(i))
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

print('-----------------------------------')
print('Total harga           : Rp {0}'.format(buy(namaBuah, banyak)))
