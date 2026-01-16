#correção do guanabra, nun sei fazer/preguiça


# PA de 10 em 10
primeiro = int(input('digite o primeiro termo: '))
razão =int(input('razão: '))
decimo = primeiro + (10 - 1) * razão 
for  c in range(primeiro, decimo + razão, razão):
    print(f'{c}', end=' > ')
print('cabo')   

