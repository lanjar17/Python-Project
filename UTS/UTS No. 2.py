#menghitung jarak tempuh pada saat t detik

def jarakTempuh():   
    t = 0
    while t <= 10:
        t += 1
        if t == 11:
            break
        
        St = (Vo * t) + (0.5 * a * t**2)
        print('t=' + str(t) ,', S(t)= ', St)


Vo = float(input('Kecepatan mula-mula(Vo) : '))#dalam m/detik
a = float(input('Percepatan(a) : '))#dalam m/detik^2

print('Jarak yang sudah ditempuh mobil untuk setiap detiknya (mulai dari t=1 hingga t=10)')
                       
jarakTempuh()
