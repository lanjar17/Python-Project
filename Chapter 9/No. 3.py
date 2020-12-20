def bintang1(n):
    for i in range(n):
        i = i+1
        print(('*' * (2*i-1)).center(2*n-1, ' '))
        
def bintang2(n):
    for i in range(n):
        i = n-i-1
        print(('*' * (2*i-1)).center(2*n-1, ' '))
        
def bintang(n):
    a = b = (n//2)+1
    bintang1(a)
    bintang2(b)

bintang(7)

    
