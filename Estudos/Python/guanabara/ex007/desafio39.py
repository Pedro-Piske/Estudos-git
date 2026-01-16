nascimento = int(input('que ano tu nasceu? '))
idade =  2024 - nascimento 
if idade < 18:
    print('mutcho novo ainda, pode alistar nao')
elif idade == 18:
    print("tá na hora de ser alistar hein zé")
elif idade > 18:
    print('xiii passou da hora, vai tomar multa por isso')
#nao quero mexer na biblioteca preguiça de ler
#   INCOMPLETO  #

from datetime import date

atual = date.today().year
nasc = int(input('ano de anscimento'))
idade = atual - nasc
print(f'quem nasceu em {nasc} tem {idade} em {atual}')
if idade == 18:
    print('tem que alistar agora zé')
elif idade < 18:
    saldo = 18 - idade
    print(f'ainda falta {saldo} anos pro alisamento') 
elif idade > 18:
    saldo = idade - 18
    print(f'voce deveria ter se alistado há {saldo} anos')