'''num = int(input('Digite um valor qualquer: '))
f = 1
soma = 0
while soma != num:
    f+=1    
    anterior = f - 1
    soma = anterior + f
    print(soma)'''
#errado, nao sei vei

#menor idiea correção

n = int(input('Quantos termos quer ver? '))
t1 = 0
t2 = 1
print(f'{t1} > {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' > {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' > FIM')

#nunca acertaria


#tentativa de cabeça, esqueci dos pritns, olhei na  resposta 5/10
n = int(input('Digite um número para a sequencia: '))
t1 = 0
t2 = 1
print(f'{t1} > {t2}', end='')
cont = 3
while cont <= n:
    t3 = t2 + t1
    t1 = t2
    t2 = t3
    print(f' > {t3}', end='')
    cont += 1
    
print(' > cabou')

