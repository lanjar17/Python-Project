def jumlah():
    data = open(myFile, "r")
    for x in data:
        x = x.split('|')
        hasil = int(x[0]) + int(x[1])
        print(hasil)
    data.close()

myFile = "bilangan.txt"
jumlah()

