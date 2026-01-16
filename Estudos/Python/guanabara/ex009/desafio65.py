n = int(input('Digite um número: '))
c = str(input('QUER continuar? [S/N]: ')).upper()
cont = 1
media = 0
soma = 0
maior = n
menor = n
while c == 'S':
    cont += 1
    soma += n
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N]: ')).upper()
    if c != 'S':
        print('muito bem, fim do programa')
    if n > maior:
         maior = n
    if n < menor:
        menor = n

media = (soma + n)/cont
print(f'Você digitou {cont} números e a media entre eles foi {media}')
print(f' o maior numero foi {maior} e o menor foi {menor}')

###dale sem guanabara


#correção do guanabara
#por algumo motivo nao funciona

resp = 'S'
soma1 = quant = media1 = maior1 = menor1 = 0 #tem que assumir maior e menor como = num, caso contrario, nao funfa
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma1 += num
    quant += 1
    if quant == 1:
        maior1 == menor1 == num
    else: 
        if num > maior1:
            maior1 = num
        if num < menor1:
            menor1 =  num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media1 = soma1 / quant 
print(f'Você digitou {quant} e a media foi {media1}')
print(f'O maior número foi {maior1} e o menor foi {menor1}')

