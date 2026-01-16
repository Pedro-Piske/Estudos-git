from datetime import date
atual = date.today().year
'''for ano in range(1, 8):
    nascimento = int(input(f'Em que ano a {ano} pessoa nasceu: '))
    maioridade = atual - nascimento
    if maioridade <= 18:
        print('menor de idade')
    else:
        print('maior de idade')'''

#incompleto

#correção do guanafodase
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a pessoa {pessoa} nasceu? '))
    Idade = atual - nasc
    if Idade >= 21:
        totmaior += 1
    else:
        totmenor -= 1
print(f'Teve {totmaior} maior de idade')
print(f'E {totmenor} menor de idade')

#cheguei tão perto de fazer igual

