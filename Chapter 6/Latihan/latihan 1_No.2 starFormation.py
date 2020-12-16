#starFormation1
def starFormation1(n):
    for baris in range (n):
        for kolom in range (baris + 1):
            print('*', end=' ')
        print()
        
starFormation1(4)


#starFormation2
def starFormation2(n):
    for baris in range (n):
        for kolom in range (4 - baris):
            print('*', end=' ')
        print()

starFormation2(4)


#gabungan keduanya
def starFormation3(n):
    for baris in range (4):
        for kolom in range (baris + 1):
            print('*', end=' ')
        print()
    for baris in range (3):
        for kolom in range (3 - baris):
            print('*', end=' ')
        print()
    
        
starFormation3(7)
