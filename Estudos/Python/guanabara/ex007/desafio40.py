nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
media = (nota1+nota2)/2
if media < 5.0:
    print(f'iiii zé tua media foi de {media} reprovou')
elif media >5.0 and media < 7.0:
    # ou 7 > media >= 5:
    print(f'ta ruinzin hein, vai pra recuperação')
elif media >= 7.0:
    print('aprovado zé')

