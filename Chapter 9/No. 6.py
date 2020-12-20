nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*63)
print('NIM'.ljust(7, ' '), 'NAMA'.ljust(10, ' '), 'N.MID'.rjust(10, ' '), 'N.UAS'.rjust(10, ' '), 'N.AKHIR'.rjust(10, ' '), 'STATUS'.rjust(10, ' '))
print('-'*63)

for data in nilai:
    akhir = (data['mid'] + 2*data['uas']) / 3
    if akhir >= 60:
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'
        
    print(data['nim'].ljust(7, ' '), data['nama'].ljust(10, ' '), str(data['mid']).rjust(10, ' '), str(data['uas']).rjust(10, ' '), str(round(akhir, 1)).rjust(10, ' '), status.rjust(10, ' '))

print('-'*63)
