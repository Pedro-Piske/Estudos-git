import random
pc = random.randint(0, 10)
contagem = 1

print('\033[1;34mEU VOU ESCOLHER UM NÚMERO DE ZERO A 10\033[m')
print('\033[1;33mTENTE ADIVINHAR\033[m')
jogador = int(input('Adivinhe: '))
if jogador == pc:
    print('\033[1;32mBoa, acertou logo de primeira\033[m')

while jogador != pc:
    jogador =int(input('\033[1;31mERROU, Tente novamente\033[m: '))
    contagem += 1
    if jogador == pc:
        print(f'\033[1;32mBOAAA você Adivinhou\nEu o número escolhi {pc}.\nForam necessarias {contagem} tentativas para acertar\033[m')


        ######LEGAL MASSSS

        #####CORREÇÃO DO GUANABARA
    
computador = random.randint(0,10)
print('SOU SEU COMPUTADOR... ACABEI DE PENSAR UM NÚMERO DE 0 A 10\nSERÁ QUE VOCÊ ADIVINHAR QUAL FOI???')
acertou = False
palpite = 0
while not acertou:
    player = int(input('Qual seu palpite: '))
    palpite += 1
    if player == computador:
        acertou = True
    else: 
        if player < computador:
            print('MAIS... Tente mais uma vez ')
        elif player > computador:
            print('MENOS... Tente Novamente')
print(f'Acertou com tantos {palpite} tentativas. BOA')