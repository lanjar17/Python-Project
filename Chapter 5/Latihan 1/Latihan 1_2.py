# program hitung syarat kelulusan

# input nilai
BahasaIndonesia = int(input('Nilai Bahasa Indonesia :'))
Matematika = int(input('Nilai Matematika :'))
IPA = int(input('Nilai IPA :'))

if(BahasaIndonesia < 0 or BahasaIndonesia > 100):
    print('Maaf input ada yang tidak valid')
elif(Matematika < 0 or Matematika > 100):
    print('Maaf input ada yang tidak valid')
elif(IPA < 0 or IPA > 100):
    print('Maaf input ada yang tidak valid')

# Status Kelulusan
elif(BahasaIndonesia > 60 and Matematika > 70 and IPA >60):
    print('Status Kelulusan : LULUS')
else:
    print('Status Kelulusan : TIDAK LULUS')
    
