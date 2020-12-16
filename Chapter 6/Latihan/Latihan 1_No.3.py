def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n-1)

def C(a, b):
    hasil = faktorial(a) / (faktorial(b) * faktorial(a - b))
    print('C','(',a,(','), b,')', '=', hasil)
    
def P(a, b):
    hasil = faktorial(a) / faktorial(a - b)
    print('P','(',a,(','), b,')', '=', hasil)


C(5, 3)
P(10, 7)
