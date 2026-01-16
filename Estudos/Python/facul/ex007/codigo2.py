#dicionarios e suas formas
dici_1 = {}
dici_1['nome'] = "Maria"
dici_1['idade'] = 25

dici_2 = {'nome': 'Maria', 'idade': 25}

dici_3 = dict([('nome', "Maria"),('idade', 25)])

dici_4 = dict(zip(['nome', 'idade'],["Maria", 25]))

print(dici_1 == dici_2 == dici_3 == dici_4)
print(dici_1)