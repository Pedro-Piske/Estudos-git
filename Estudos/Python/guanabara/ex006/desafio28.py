import random
e1 = int(input("Digite um numero de 1 a 5: "))
e2 = int(input("Digite um numero de 1 a 5: "))
e3 = int(input("Digite um numero de 1 a 5: "))
e4 = int(input("Digite um numero de 1 a 5: "))
e5 = int(input("Digite um numero de 1 a 5: "))
escolhido =[e1, e2, e3, e4, e5]
escolha = random.choice(escolhido)
Minha_escolha = int(input("Tente adivinhar o numero escolhido pelo pc: "))
print(escolha)
if escolha == Minha_escolha:
    print("Você acertou, boa demias")
else:
    print("Ai que burro, da zero pra ele")



#correção do guagua


import time
computador = random.randint(0,5)
print('-=-' * 20)
print("Adivinhe o numeor que escolhi entre 0 e 5")
print('-=-' * 20)
jpgador = int(input("Adivinhe: "))
print("PROCESSANO...")
time.sleep(4)
if jpgador == computador:
    print("Quanta gameplay")
else:
    print("Erro burrão")

