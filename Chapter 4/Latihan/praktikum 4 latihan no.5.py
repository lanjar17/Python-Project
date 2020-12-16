#program grafik diagram

print("grafik diagram batang horizontal mahasiswa laki-laki dan perempuan")
lakilaki = int(input("masukkan jumlah mahasiswa laki-laki : "))
perempuan = int(input("masukan jumlah mahasiswa perempuan : "))

mahasiswa = int(lakilaki / 10)
mahasiswi = int(perempuan / 10)

print("laki-laki : ", '*' * mahasiswa)
print("perempuan : ", '*' * mahasiswi)
