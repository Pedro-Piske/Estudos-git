'''num = int(input('Digite um número para calcular seu fatorial: '))

while num !=1:
    num1 = num - 1
    fatorial = num*num1
print(f'O fatorial é {fatorial}')'''

########### nao cosngi oresovler
        

    #CORREÇÃO DO GUANABARA

from math import factorial

n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')



### ou

n2 = int(input('Digite um número para calcular seu fatorial: '))
c = n2
f = 1
print(f'calculando {n2}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'O fatorial de {n2} é {f}')

