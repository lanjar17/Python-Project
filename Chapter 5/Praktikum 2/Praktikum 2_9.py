from random import randint
sum = 0
while True:
    bil = randint(0, 10)
    print(bil)
    sum = sum + 1
    if bil == 5:
        break
print('Jumlah Perulangan : ' + str(sum))
