
'''nome = continuar = str
preço  = p1000 = barato = nomebarato = total = 0
while True:
    print('LOJA CARA PRA CARAI, AQUI TU FICA SEM DINHEIRO ')
    nome = str(input('Nome do produto: '))
    preço = int(input('Valor do produto: '))

    barato = preço
    if preço < barato:
        barato = preço
        nomebarato = nome
    if preço >= 1000:
        p1000 += 1

    total = preço + total


    continuar = str(input('Deseja adicionar algo a mais? [S/N]')).upper().strip()[0]

    if continuar == 'N':
        break

print(f'total da compra foi {total}')
print(f'A quantidade de itens acima de mil reais: {p1000}')
print(f'O item mais barato foi {nomebarato} custou {barato}')
'''
#imcompleto item barato nao funciona nessa porra


#CORREÇÃO DO GUANABARA
total = tot1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    total += preço
    cont += 1
    if preço > 1000:
        tot1000 +=1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
   
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')    
print(f'Temos {tot1000} produto custando mais de R$1000.00')
print(f'O produto mais barato foi de {barato} que custa R${menor:.2f}')