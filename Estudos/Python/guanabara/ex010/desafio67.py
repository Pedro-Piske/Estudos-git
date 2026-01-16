c = 0
n = int(input('Digite um número para ver sua tabuada: '))
while c != 11:
    print(f'{n} x {c} = {n*c}')
    c+=1
print('fim do programa')

## incompleto

###correção do guanabara
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    for multiplicador in range(1, 11):          # isso aqui é doiediera, for dentro do while, cabecinha nunca que acertava
        print(f'{num} x {multiplicador} = {num*multiplicador}')
    print('-'*30)
print('fim do programa, volte sempre')