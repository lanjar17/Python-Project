# program hitung syarat kelulusan

# input nilai
# Bahasa Indonesia
BahasaIndonesia = int(input('Nilai Bahasa Indonesia :'))
if(BahasaIndonesia >= 0 and BahasaIndonesia <= 100):

# Matematika
    Matematika = int(input('Nilai Matematika :'))
if(Matematika >=0 and Matematika <= 100):

# IPA
    IPA = int(input('Nilai IPA :'))
if(IPA >=0 and IPA <= 100):


# Status Kelulusan
    if(BahasaIndonesia > 60 and IPA > 60 and Matematika > 70):
        print('Status Kelulusan : LULUS')
    else:
        print('Status Kelulusan : TIDAK LULUS')
    
