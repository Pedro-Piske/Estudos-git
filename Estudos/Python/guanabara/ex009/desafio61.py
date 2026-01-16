'''p = int(input('Digite o primeiro termo: '))
razão = int(input('Agora digite a razão dessa PA: '))
c = 0
while c == 10:

    c += 1'''
#menor ideia de como continuar


#CORREÇÃO DO FODA

primerio = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primerio
cont = 1
while cont <= 10:
    print(f'{termo} > ', end='')
    termo += razão
    cont += 1
print('CABO')