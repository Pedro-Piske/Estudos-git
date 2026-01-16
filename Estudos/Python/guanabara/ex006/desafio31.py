km = int(input("Quantos quilometros tu vai viajar? "))
if km <= 200:
    passagem = km* 0.5
    print(f"A passsagem será {passagem} reais")
else:
    passagem2 = km * 0.45
    print(f"Como você vai viajar mais de 200km, a passagem será {passagem2} reias")

# Segunda Form #
distancia = float(input("Distnacia da viagem: "))
preço = distancia * 50 if distancia <=200 else distancia * 0.45
print(f"valor da passagem é {preço}")