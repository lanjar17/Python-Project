def caesar(teks, key):
    hasil = ' '
    data = open(teks, "r")
    for i in data.read():
        if i == ' ':
            hasil += i
        elif i.islower():
            hasil += chr((ord(i) + key - 97) % 26 + 97)
        else:
            hasil += chr((ord(i) + key - 65) % 26 + 65)
    data.close()
    enc = open(teks + ".encrypt", "w")
    enc.write(hasil)
    enc.close()
    print('\nFile enkripsi : {}.encrypt'.format(teks))

teks = input('Nama file yang ingin di enkripsi : ')
key = int(input('Input key : '))
caesar(teks, key)
