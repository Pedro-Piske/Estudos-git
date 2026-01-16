from datetime import date # importando pra saber se ano atual é bissexto
ano_bi = int(input("Digite um ano ai pra ver se é bissexto, 0 pra ver se o ano atual é bissexto "))
if ano_bi == 0:
    ano_bi = date.today().year # pra analisar o ano atual do teste
if ano_bi & 4 == 0 and ano_bi % 100 != 0 or ano_bi % 400 == 0:
    print("ano bissexto")
else:
    print("ano normal zé")