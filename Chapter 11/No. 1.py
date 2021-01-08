from datetime import *

def diffDate(x):
    skrg = datetime.date(datetime.now())
    print('Tanggal hari ini : ', skrg)
    
    x = x.split('-')
    x = date(int(x[0]), int(x[1]), int(x[2]))
    print('Tanggal x        : ', x)
    
    selisih = (x - skrg).days
    print('Selisih          : ', selisih, 'hari')
    return selisih

diffDate('2021-12-31')
