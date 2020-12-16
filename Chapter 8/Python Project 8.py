def rerataHarga():
    harga = list(buah.values())
    total = 0
    banyak = 0
    for i in harga:
        total += i
        banyak += 1
    rata2 = total/banyak
    return rata2

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print(rerataHarga())
