import random
'''Escolha = int(input('1 TESOURA\n2 PEDRA\n3 PAPEL\nESCOLHA '))
pc = random.randint(1,3)
if Escolha == pc:
    print(f'escolhi {pc} logo empatamos')
elif Escolha == 1 and pc == 2 or Escolha == 2 and pc == 3 or Escolha == 3 and pc == 1:
    print(f'escolhi {pc}, perdeu trouxa')
elif Escolha == 1 and pc == 3 or Escolha == 2 and pc == 1 or Escolha == 3 and pc == 2:
    print(f'escolhi {pc}, logo perdi, gg')
else:
    print('escolheu numero errado zé')'''

## forma so que boitno ##

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0,2)
print('''Suas opções
[0] Pedra
[1] Papel
[2] Tesoura              ''')
jogador = int(input('Escolha: '))

if jogador == computador:
    print('\033[1;33mEMPATE\033[m')
elif jogador == 1 and computador == 0 or jogador == 2 and computador == 1 or jogador == 0 and computador == 2:
    print('\033[1;32m VENCEU\033[m')
elif jogador == 1 and computador == 2 or jogador == 2 and computador == 0 or jogador == 0 and computador == 1:
    print('\033[1;31m PERDEU\033[m')
else: 
    print('OPÇÃO INVALIDA')
print(f'\033[4;36mO computador escolheu {itens[computador]} e você escolheu {itens[jogador]}\033[m')

#####correçao do guagua#####




from time import sleep
itens1 = ('PEDRA', 'PAPEL', 'TESOURA')
computador1 = random.randint(0,2)
print('''Suas opções
[0] Pedra
[1] Papel
[2] Tesoura              ''')
jogador1 = int(input('Escolha: '))

print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA!!!')
sleep(1)
print(f'\033[4;36mO computador escolheu {itens1[computador1]} e você escolheu {itens1[jogador1]}\033[m')
if computador1 == 0:
    if jogador1 == 0:
        print('EMPATE')
    elif jogador1 == 1:
        print('JOGADOR VENCE')
    elif jogador1 == 2:
        print('COMPUTADOR VENCE')
    else: print('JOGADA INVALIDA')

elif computador1 == 1:
    if jogador1 == 0:
        print('COMPUTADOR VENCE')
    elif jogador1 == 1:
        print('EMPATE')
    elif jogador1 == 2:
        print('JOGADOR VENCE')
    else:
        print('INVALIDO')

elif computador1 == 2:
    if jogador1 == 0:
        print('JOGADOR VENCE')
    elif jogador1 == 1:
        print('COMPUTADOR VENCE')
    elif jogador1 == 2:
        print('EMPATE')
else: 
    print('JOGADA INVALIDA')

