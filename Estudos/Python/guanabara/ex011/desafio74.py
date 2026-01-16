from random import randint
'''menor = maior = 0
for c in range(0, 5):
    n = randint(0, 10)
    print(n, end=' ')
    if n == 1:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'\nO maior numero é {maior}')
print(f'O menor número é {menor}')'''



    #Erro na linha do menor, refazer na correção


#CORREÇÃO
numeros = ( randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os números sorteados foram: ', end='')
for numero in numeros:
    print(numero, end=' ')
print(f'\nO maior número foi {max(numeros)}') #max pra achar o maior número
print(f'O menor número foi {min(numeros)}')  # min pra achar o menor número
#Nao tenho certeza como funciona o min e o maxb