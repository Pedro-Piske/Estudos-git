'''cardapio = 'Bergamota', 5.70, 'Só Canela', 99.90, 'Manjericão', 50, 'Angustia', 9.99
print(cardapio)
'''
#incopetente

#correção

listagem = 'Caderno', 12.90, 'Lapis', 2.00, 'Mochila', 49.99, 'Caneta', 5.00
print('-'*30)
print(f'{"BEM VINDO A LOJINHA":^15}') #essa fomra de centralizar nao ta funfando
print('-'*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:    
        print(f'{listagem[pos]:.<23}', end='')
    else:
        print(f'R${listagem[pos]}')
print('-'*30)