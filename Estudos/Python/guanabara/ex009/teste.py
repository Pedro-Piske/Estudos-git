c = 1
while c < 10:
    print(c)
    c += 1
print('fim')


#USAR WHILE QUANDO NAO SABE O LIMITE
#PODE USAR O WHILE QUANDO SABE O LIMITE TAMBEM
r = 'S'
while r == 'S':
    n = int(input('digite um valor '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('fim')

################
num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares')