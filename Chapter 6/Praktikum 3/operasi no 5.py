from operation import *

# a
a = 2
b = 4
c = 6
j = kali(b, c)
k = kurang(a, b)
l = jumlah(j, k)
print('a.',a, '+', b, 'x', c, '-', b, '=', l)


#b
a = 4
b = 6
c = 7
d = 9
j = jumlah(a, c)
k = kurang(b, d)
l = kali(j, k)
print('b.(',a, '+', c, ')x(' ,b, '-', d, ')=', l)


#c
a = 2
b = 5
c = 7
d = 10
e = 12
f = 34
j = jumlah(d, a)
k = jumlah(c, b)
l = kurang(e, f)
m = bagi(jumlah(d, a), jumlah(c, b))
n = bagi(m, l)         
print('c. (',d, '+', a, ')/(' ,c, '+', b, ')/(' ,e, '-', f, ')=', n) 
