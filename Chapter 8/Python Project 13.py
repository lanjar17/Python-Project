nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def Mhs(nilaiMhs):
    nilai = 0
    for i in nilaiMhs:
        mid = i.get('mid')
        uas = i.get('uas')
        nilaiAkhir = (mid + 2*uas)/3
        if nilaiAkhir > nilai:
            nilai = nilaiAkhir
            data = {}
            data['nim'] = i.get('nim')
            data['nama'] = i.get('nama')
    return data

Mhs(nilaiMhs)
tertinggi = Mhs(nilaiMhs)
print('NIM {0} dan Nama {1} memiliki nilai akhir tertinggi'.format(tertinggi['nim'], tertinggi['nama']))
