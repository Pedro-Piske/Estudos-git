#tuplas sao imutaveis

lanche = ('Cu de curioso', 'Mika Gay', 'Ronaldo fenomeno', 'Masarico')
print(lanche[2]) # exibwe o ronaldo fenomeno 
print(lanche[-3]) #Exibe o mika gay
print(lanche[1:3]) #exibe mika gay e ronaldo fenomeno
print(lanche[2:]) #exibe ronaldo fenomeno e masarico
print(lanche[:2]) #exibe cu de curioso e mika gay

#tuplas sao imutaveis

for cont in range(0, len(lanche)):
    print(f'Eu vou comer o {lanche[cont]} na posição {cont}')

    #ou

for comida in lanche:
    print(f'Eu vou comer o {comida}')

    #ou

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')    
print('Enchi o bucho')