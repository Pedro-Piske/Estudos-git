#calculadora de desconto
valor_produto = float(input("digite o valor do produto: R$ "))
percentural_desconto = float(input("digite o percentual do desconto: "))
if percentural_desconto < 0 or percentural_desconto > 100: 
    print("erro, desconto invalido")
else:
    desconto = valor_produto * (percentural_desconto / 100)
valor_final = valor_produto - desconto
print(f"valor do desconto é {valor_final:.2f}")