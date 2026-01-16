num =(input('Digite um número: '))
num2 = ','.join(num)
print(f'Unidade: {num2[6]}')
print(f'Dezena {num2[4]}')
print(f'Centena {num2[2]}')
print(f'Milhar {num2[0]}')
print(num2)

#guanabara correção

num1 = int(input('digite um numero vei de 4 digitos: '))
uni = num1 // 1 % 10
de = num1 // 10 % 10
cen = num1 // 100 % 10
mil = num1 // 1000 % 10
print(f'Unidade: {uni}')
print(f'Dezena: {de}')
print(f'Centena: {cen}')
print(f'Milhar: {mil}')
