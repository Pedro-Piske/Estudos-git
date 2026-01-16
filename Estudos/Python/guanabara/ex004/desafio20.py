import random
n1 = input('Digite um nome: ')
n2 = input('Digite outro nome: ')
n3 = input('Digite mais um nome: ')
n4 = input('Digite um ultim nome: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)