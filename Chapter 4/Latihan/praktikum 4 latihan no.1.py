# program hitung tarif rental

tarif1 = 200000
tarif2 = 10000
jamMulai = 6
menitMulai = 00
jamSelesai = 23
menitSelesai = 50

lamaSewajam = jamSelesai - jamMulai
lamaSewamenit = menitSelesai - menitMulai

totalWaktu = int(lamaSewajam + lamaSewamenit / 60)

totalbiaya = int(tarif1 + tarif2 * (totalWaktu - 12))

print("total tarif ", totalbiaya)

