def mhs(myFile):
    data = open(myFile, "r")
    mhs = data.read().splitlines()
    dataMhs = {}
    key = 1
    for i in mhs:
        x = i.split('|')
        dataMhs[key] = {'nim': x[0], 'nama': x[1], 'alamat': x[2]}
        key += 1
    print(dataMhs)
    return dataMhs

myFile = "dataMhs.txt"
mhs(myFile)
