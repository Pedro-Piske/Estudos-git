import math
co = int(input('valor do cateto oposto '))
ca = int(input('Valor do cateto adjacente '))
hip= (co **2 + ca **2)** (1/2)
print(f'{hip:.2f}')

co2 = float(input('cateto oposto '))
ca2 = float(input('cateto adjancente '))
hi = math.hypot(co2, ca2)
print(hi)