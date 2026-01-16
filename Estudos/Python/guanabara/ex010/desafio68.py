from random import randint
'''print('JOGO DO IMPAR OU PAR')
escolha = str(input('ESCOLHA [IMPAR/PAR]: ')).upper().strip()[0]
pc = random.randint(1,10)
jogador = int (input('Digite o número que vai jogar: '))
soma = jogador + pc
impar = jogador % 2 == 1
par = jogado
par1 = soma % 2 == 0
impar1 = soma % 2 == 1 

print(f'o resultado foi {soma}')
print(f'eu escolhi {pc}')

if escolha == 'IMPAR': 
    print('Você escolheu impar, ganhou')

elif escolha == 'PAR':
    print('Vc escolheu par, ganhou')
else:
    print('eu venci')'''

### desisto

# correção nao funciona direito
v = 0
while True:
    jogador = int(input('Diga um valor: '))   
    pc = randint(0, 10)
    soma = pc + jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Você vai escolher impar ou par? [P/I] ')).upper().strip()[0]
        print(f'Você escolheu {jogador}, Eu escolhi {pc} a soma disso é {soma}')
        print('Deu par' if soma % 2 == 0 else 'Deu impar')
        if escolha == 'P':
            if soma % 2 == 0:
                print('VOCÊ VENCEU')
                v+= 1
            else:
                print('Voce perdeu')
                break
        elif escolha == 'I':
            if soma % 2 == 1:
                print('Você Venceu')
                v+=1
            else:
                print('Voc^^e perdeu}')
                break
        print('Vamos jogar novamente')
print(f'Você venceu {v} vezes, mas isso termina aqui')