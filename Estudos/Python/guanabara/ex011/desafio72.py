num = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUARTOZE', 'QUINZE', 'DEZESSEIS', 'DEZESETE', 'DESSOITO', 'DEZENOVE', 'VINTE')

escolha = int(input('Escolha um número de 0 a 20: '))

while escolha < 0 or escolha > 20:
    escolha = int(input('Tente novamente. Escolha um número de 0 a 20: '))

 
print(f'Você digitou o número {num[escolha]}')


#incompleto
# corrigir uma coisa e agora funfa  

#CORREÇÃO

cont = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUARTOZE', 'QUINZE', 'DEZESSEIS', 'DEZESETE', 'DESSOITO', 'DEZENOVE', 'VINTE')
continuar = str
while True:
    n = int(input('Digite um número de 0 à 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente', end='')
print(f'Você digitou o número {cont[n]}')

