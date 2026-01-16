
sexo = str(input('Qual seu seuxo? [M/F]: ')).upper().strip()
if sexo == 'mM' or sexo == 'fF':
    print(f'Sexo {sexo} registrado')

else:
    while sexo != 'Mm' or sexo != 'Ff': #nao ffunciona pro causa dessa idiotice aqui, use not in seu animal
        print(f'{sexo} não é um valor valido')
        print('Insira M para masculino ou F para femenino')
        sexo = str(input('Qual seu sexo? [M/F]: ')).upper().strip()
#seila pq essa porra nao funciona

#correção do guanafoda

s = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Dados inválidos. Por favor tente novamente: [M/F]')).upper().strip()[0]
print('Dados recebidos com sucesso')