print("Pak Amir menempuh waktu dari kota A ke C adalah?")

waktuAwal = float(06.00)
waktuJeda = float(0.45)

jarakAB = int(125)
jarakBC = int(256)

kecepatan1 = int(62)
kecepatan2 = int(70)

waktuAB = round(jarakAB/kecepatan1)
waktuBC = round(jarakBC/kecepatan2)

waktusampai = waktuAwal + waktuAB + waktuBC + waktuJeda
print("waktu sampai di kota C => pukul", waktusampai)
