frase = 'Curso em Video Python'
frase[9]
frase[9:13]# vai parar na letra 12
frase[9:21:2] #vai parar na caractere 21 de 2 em 2
frase[:5] # começa do zero e para no 4
frase[15:] #inicia do 15 até o final
frase[9::3] #vai começar no nove até o final de 3 em 3

len(frase) # ler o comprimento da frase
frase.count('o')#conta a quanitdade de o na frase
frase.count('o',0,13)#conta os o do zero até o 12
frase.find('deo')#encontra onde está o deo
frase.find('Android')#str que nao existe recebe -1
'Curso' in frase # vai procurar a str e resulta em true ou false

frase.replace('Python','Android')#substitui a primeira plavra pela segunda
frase.upper()#deixa tudo em maisculo
frase.lower()#deixa tudo em minusculo
frase.capitalize()#deixa tudo minusculo menos a primeira letra da str
frase.title()#deixa todas as primieras letras das palavras em maiusculo

frase.strip()#remove espaços inuteis na str
frase.rstrip()#remove os ultimos espaços
frase.lstrip()#remove os primieros espaços

frase.split() #divide de acordo com os espaços, criando varias listas
'-'.join(frase) # Adiciona um caracter em toda a str

print(""" """)# use pra textão
