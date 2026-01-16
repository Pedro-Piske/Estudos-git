#mutcho difcil zé voi pegar correçaõ so44


###         CORREÇÃO DO GUANAFODDASE        ###

num = int(input('Digite um número inteiro: '))
print('''Escolha um das bases pra conversão:
[1] converter em Binário
[2] converter para Octal
[3] converter para Hexadecimal''')
opção = int(input('sua opção: '))
if opção == 1:
    print(f'{num} convertido para binário é igual {bin(num)[2:]}') # usar 2: pra tirar letra feia no inicio da resposta
elif opção == 2:
    print(f'{num} convertido para binário é igual {oct(num)[2:]}') # duvidas tirar 2: 
elif opção == 3:
    print(f'{num} convertido para binário é igual {hex(num)[2:]} ')
else:
    print('numero invalido zé')
