s = 0
for num in range(1, 7):
    cacilda = int(input('Digite valores sue corno: '))
    if cacilda % 2 == 0:
        s = s + cacilda
print(s)

    #errado
    #parece funcional agora, a mente clareia antes da resolução do guaguau

#falando no diabo, correção
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'digite um {c} valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'vc informou {cont} numeros pares e a soma foi {soma}')