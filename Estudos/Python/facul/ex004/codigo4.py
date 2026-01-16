#inputs
email = input("escreva seu email: ")
nome = input("seu primeiro nome: ")
print(nome, email)
print(f"{nome},verifique seu email: {email} que enviamos um link de confirmação")

faturamento = int(input("escreva o faturamento: "))
imposto = faturamento * 0.1
print(imposto)

#listas
vendas = [100, 400, 3, 33, 55, 43]
total_vendas = sum(vendas)
print(total_vendas)

quantidade_vendas = len(vendas)
print(quantidade_vendas)
print(max(vendas))
print(min(vendas))