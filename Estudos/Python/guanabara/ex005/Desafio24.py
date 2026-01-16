cidade = input('Digite um nome de cidade: ')
cidade2 = cidade.title()
primeiro ='Santo' in cidade2
print(primeiro)

#correção guanafodase
cid = str(input('Em que cidade vc nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')