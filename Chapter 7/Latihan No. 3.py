sum = 0
i = 0
print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')

while True:
    try:
        bilangan = int(input('Masukan bilangan bulat : '))
    except ValueError:
        print('Bukan bilangan bulat')
        continue
    
    sum += bilangan
    i += 1
    rata2 = sum/i
    jawab = input('Lagi (y/n)? : ')
        
    if jawab == 'n':
        break
    
print('-----------------------------')
print('Rata-ratanya adalah : ', rata2)
