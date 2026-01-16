import random
a1 = input('Digite um nome: ')
a2 = input('Digite outro nome: ')
a3 = input('Digite mais um nome: ')
a4 = input('Digite um ultimo nome: ')
aluno = [a1, a2, a3, a4]
escolhido = random.choice(aluno)
print(f'Nome escolhido foi {escolhido}')