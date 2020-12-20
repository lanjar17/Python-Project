def bintang(n):
    for i in range(n):
        i = i+1
        print(('*' * (2*i-1)).center(2*n-1, ' '))
        
bintang(4)
