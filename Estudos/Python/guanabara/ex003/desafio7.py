m1 = float(input("Primeira nota: "))
m2 = float(input('Segunda nota: '))
media_final = (m1 + m2)/2
if media_final < 5:
    print('reprovado')
else:
    print('aprovado')
print(f"A media final foi {media_final:.2}")