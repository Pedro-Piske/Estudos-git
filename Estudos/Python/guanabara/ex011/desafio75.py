'''cont = 0
a = int(input('Digite primeiro valor: '))
b = int(input('Digite segundo valor: '))
c = int(input('Digite terceiro valor: '))
d = int(input('Digite o ultimo valor: '))
valores = (a, b, c, d)
print(valores)
if 9 in valores:
    print(f'Foram contados {cont} números 9')

if 3 in valores:
    print(f'O 3 está na posição {valores.index(3)+1}')
else:
    print('Não há números 3 nessa tupla')'''

#nao sei mais como continuar
#incompleto

#CORREÇÃO

n = (int(input('Digite um valor: ')), int(input('Digite segundo valor: ')),
      int(input('Digite mais um valor: ')), int(input('Digite um ultimo valor: ')))
print(n)
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 está na posição {n.index(3)+1}')
else:
    print('O valor 3 não apareceu nenhuma vez')   

 #essa parte ta dando erro, deve ser pq hj nao funfa mais
'''print('O números de pares digitados é: ', end='')
for num in n:
     if n % 2 == 0:
        print(num, end=' ')'''

    