def myPrice():
    global buah
    harga = list(buah.values())
    harga.sort(reverse=True)
    mahal = harga[0]
    for buah, harga in buah.items():
        if harga == mahal:
            return buah

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print(myPrice())
