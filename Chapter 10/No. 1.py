def read(myFile):
    bil = open(myFile, "r")
    genap = 0
    ganjil = 0

    for data in bil:
        if int(data) % 2 == 0:
            genap = genap + 1
        else:
            ganjil = ganjil + 1

    bil.close()
    hasil = {"genap" : genap, "ganjil" : ganjil}
    return hasil

myFile = "databil.txt"
print('Banyak bilangan genap: ', read(myFile).get("genap"))
print('Banyak bilangan ganjil: ', read(myFile).get("ganjil"))
