convidados = ("pedrinho","joaozin","rebecao","jorgin")
confirmados = ["pedrinho","rebecao"]
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]
print('convidados que ainda não confirmaram:')
for pessoa in nao_confirmados:
    print(pessoa)