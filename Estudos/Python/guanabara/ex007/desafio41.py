from datetime import date
nascimento = int(input('teu ano de nascimento zé: '))
ano = date.today().year
idade = ano - nascimento  
if idade <= 9:
    print('Nadador mirim')
elif idade <= 14:
    print('Nadador infantil')
elif idade <=19:
    print('Nadador junior')
elif idade <= 25:
    print('Nadador senior olha só')
elif idade > 25: # ou else
    print('O brabo tem nome, um mestre')
print(f'pois ele tem {idade} anos')