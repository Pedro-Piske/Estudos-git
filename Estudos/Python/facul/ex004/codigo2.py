faturamento = 1000
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento
margem_lucro = round(margem_lucro, 2)
print(f"faturamento da empresa {faturamento}, custo: {custo} lucro: {lucro} margem{margem_lucro:.0%}")



email_cliente = "porqueiravelha@gmail.com"
#letra tudo maisculo = upper
email_cliente = email_cliente.upper()
print(email_cliente)
#letra tudo minuscula = lower
email_cliente = email_cliente.lower()
print(email_cliente)
#procura letra no texto = find
print(email_cliente.find("@")) 
# seila o que isso faz
print(len(email_cliente))
#pega um caracter
print(email_cliente[0])

print(email_cliente[-5])
#corta texto
print(email_cliente[:14])
#troca texto
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
print(novo_email)

nome = "pedrinho mata newba"
#capitalize primeira letra da frase maiscula, e title todas as primeiras letras maiusculas
print(nome.capitalize())
print(nome.title())

posição_arroba = email_cliente.find('@') + 1
servidor = email_cliente[posição_arroba:]
print(servidor)

posicao_espaço = nome.find(" ")
primeiro_nome = nome[:posicao_espaço]
sobrenome = nome[posicao_espaço:]
print(primeiro_nome)
print(sobrenome)

