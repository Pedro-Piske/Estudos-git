#PRESENÇA DIVINA FAZ ISSO FUNCIONA, NAO MEXA

# sem presença divina, apenas 2 num faz a flag ser anulada
num = int(input('Digite um número: '))
num1 = 0
cont = 1
while num != 999:
    num1 += num
    num = int(input('Digite mais um número: '))
    cont += 1
print(f'A soma dessses números foi {num1}')
print(f'O número tota de números foi de {cont - 1}')


## correção do guanabara
n = 0
cont = 0
soma = 0
n = int(input('digite um número [999 para parar]'))
# ou n = cont = soma = 0
while n != 999:
    soma += n 
    cont += 1
    n = int(input('digite um número [999 para parar]'))
print(f'Vc digitou {cont} numeros e a soma entre eles foi {soma}')