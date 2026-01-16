carros = ['Chiron', 'Laferrari', 'Corsa', 'Landau']
for carro in carros:
    print(f'Posição = {carros.index(carro)}, carro = {carro}')
#nao sei como funciona, mais sei que lower é usado para minuscular as cosia
carros = [item.lower()for item in carros]
print("\ncarro = ",carros)
