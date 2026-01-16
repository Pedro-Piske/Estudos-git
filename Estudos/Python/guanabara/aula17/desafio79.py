valor = valor2 = []
while True:
    valor.append(int(input('Digite um valor: ')))
    valor2 = valor[:]

    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
#incompleto     
print(sorted(valor))
print(valor2)