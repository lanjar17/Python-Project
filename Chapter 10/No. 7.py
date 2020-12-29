def caesar(teks, key):
    hasil = ' '
    data = open(teks, "r")
    for i in data.read():
        if i == ' ':
            hasil += i
        elif i.islower():
            hasil += chr((ord(i) - key - 97) % 26 + 97)
        else:
            hasil += chr((ord(i) - key - 65) % 26 + 65)
    data.close()
    dec = open(teks + ".decrypt", "w")
    dec.write(hasil)
    dec.close()
    print('\nFile dekripsi : {}.decrypt'.format(teks))

teks = input('Nama file yang ingin di dekripsi : ')
key = int(input('Input key : '))
caesar(teks, key)
