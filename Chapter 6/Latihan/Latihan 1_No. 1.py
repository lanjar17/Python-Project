def isPythagoras(a, b, c):
    if(a**2 + b**2 == c**2):
        print('a =', a, 'b =', b, 'c =', c, '->', True)
    else:
        print('a =', a, 'b =', b, 'c =', c, '->', False)

isPythagoras(3, 4, 5)
isPythagoras(5, 9, 12)
isPythagoras(8, 6, 10)
isPythagoras(7, 8, 11)
