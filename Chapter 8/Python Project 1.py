import random
while True:
    try:
        n = int(input('Berapa bilangan yang di inginkan : '))
        break
    except:
        print('Masukan angka saja')
        continue
print('Silahkan input {0} bilangan'.format(n))

bilangan = []
while n > 0:
    while True:
        try:
            bil = int(input('Masukan bilangan bulat : '))
            break
        except:
            print('Bukan bilangan bulat')
            continue
    bilangan = bilangan + [bil]
    i = None
    while i != 1:
        i = random.randint(0, 10)
    n += i - i - i
bilangan.sort()
print('Urutan bilangan dari yang terkecil')
for x in bilangan:
    print(x)
