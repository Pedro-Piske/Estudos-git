soma = 0
for impares in range(1, 500):
    if impares % 2 == 1:
        if impares % 3 == 0:
            soma = soma + impares
print(soma)

#correlçao do aguanavara
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        soma = soma + c
print(f'a soma de todos os {contador} valores impares é {soma}')
