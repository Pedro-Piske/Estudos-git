lanche = ('Macarrão', 'Camarão', 'Caramujo')
print(sorted(lanche)) #mostra lanche em ordem alfabetica

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(sorted(c))
print(c.count(5)) # Conta a quantidade de 5 na tupla
print(c.index(4)) # Mostra a posição do 4
print(c.index(5, 1)) # Mostra a posição do 5 a partir do elemento 1

pessoa = ('Pedrada', 20, 'M', 82.55) # NO PYTHON PODE USAR VARIOS TIPOS DE ELEMENTOS NA MESMA TUPLA 
print(pessoa)
del(pessoa) # PRA DELETAR A TUPLA