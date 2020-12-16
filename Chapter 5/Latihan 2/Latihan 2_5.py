print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
Tebakan = int(input('Tebakan Anda : '))
while True:
    if(Tebakan < 10):
        print('Hehehe… Bilangan tebakan anda terlalu kecil')

        Tebakan = int(input('Tebakan Anda : '))
    elif(Tebakan > 10):
        print('Hehehe… Bilangan tebakan anda terlalu besar')

        Tebakan = int(input('Tebakan Anda : '))
    elif(Tebakan == 10):
        print('Yeeee… Bilangan tebakan anda BENAR :-)')
        break
    
    

    
          
