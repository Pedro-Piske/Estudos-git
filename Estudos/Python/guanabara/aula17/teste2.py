valores = []
'''for v in valores:
    print(f'{v} ', end='')'''
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')

a = [1, 3, 5, 7]
b = a[:] # USAR ISSO PRA FAZER UMA COPIA, USAR B = A NAO FUNCIONA
b[3] = 0
print(a)
print(b)