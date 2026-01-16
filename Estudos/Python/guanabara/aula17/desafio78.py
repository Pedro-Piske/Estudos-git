lista = []
cont = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
    cont += 1
print(f'Os valores digitados foram {lista}')

print(f'o maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor digitado foi o {min(lista)} na posição {lista.index(min(lista))}')

#incompleto, nao sei colcoar pra varias posições