'''lista = 'Dupla', 'America', 'Linguagem', 'Mercado', 'Dinossauro', 'prprp', 'Medonho', 'cocorico', 'RWRWR'
vogal = 'aeiou'
for c in lista:
    if 'a' in c:
        print(f'Na palavra {c} tem vogal {''}')
    else:
        print(f'Não tem vogal na palavra {c}')

#nao sei como finalizar'''
#correção, cheguei perto vai
palavra =  'Dupla', 'America', 'Linguagem', 'Mercado', 'Dinossauro', 'prprp', 'Medonho', 'cocorico', 'RWRWR'
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ') 
    