
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite mais um valor: '))
opção = 0

while opção != '5':
    opção = str(input('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA \nEscolha: '))
    if opção == '1':
        soma = num1 + num2
        print(f'A soma desses dois números é {soma}')
    if opção == '2':
        multi = num1 * num2
        print(F'A multiplicação desses dois números é {multi}')
    if opção == '3':
        if num1 < num2:
            print(F'O número {num2} é o maior número')
        else:
            print(f'O número {num1} é o maior número')
    if opção == '4':
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite mais um valor: '))
    
    #correção do gauanbeara
    # nao funcioan por forçã maior


n1 = int(input('Primeiro valor: '))   
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa ''')
    opção = int(input('Qual é sua opção? '))
    if opção == 1:
        
        soma == n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opção == 2:
        
        produto == n1 * n2
        print(f'O resultado de {n1} x {n2} é de {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(F'Entre {n1} e {n2} o maior é {maior}')
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segundo Número: '))
    elif opção == 5:
        print('Finalizando...')
    
    else:
        print('Opção invalida')
print('Fim do programa, volte sempre')