#deasfio 52
'''num = int(input('Digite um número: '))
for primo in range(1, num):'''


    #menor ideia

#correção do guanabara

num = int(input('digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\nO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('É primo')
else:
     print('é primo não zé')
#MUITO CUIDADO COM NUMERO GRANDES, PODE CONSUMIR MUITA RAM