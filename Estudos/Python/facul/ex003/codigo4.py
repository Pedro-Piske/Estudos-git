notas = [5.6,10.0,6.9,7.0,3.0]
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media
arredodar_media = lambda media: round(media,2)
media = calcular_media(notas)
media_arrendondada = arredodar_media(media)

situação = "aprovado" if media_arrendondada>=7 else "reprovado"

print(notas)
print(media_arrendondada)
print(situação)