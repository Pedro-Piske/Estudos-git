'''peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 > imc < 25:
    print('ta no peso certo zé')
elif 25 > imc < 30:
    print('ta acima do peso hien zé')
elif 30 > imc < 40:
    print('cacete mano, faz um dieta')
elif imc > 40:
    print('nuuuuuuh gordo demais que porra é essa')'''

#tudo errado zé
#pega a correçâo do guagua

p = float(input('qual é seu peso em kg? '))
al = float(input('qual sua altura em metros? '))
imc2 = p / (al**2)
print(f' o imc dessa pessoa é de {imc2:.1f}')
if imc2 < 18.5:
    print('abaxio do peso zézin')
elif 18.5 <= imc2 < 25:
    print('faixa de peso bacana')
elif 25 <= imc2 < 30:
    print('voce está em sobrepeso')
elif 30 <= imc2 < 40:
    print('ta obeso mané, treinar né')
elif imc2 >=40:
    print('cacete gigante baleia enorme puts que apriu')
