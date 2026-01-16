faturamento = 1000
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento
margem_lucro = round(margem_lucro, 2)
print(f"faturamento da empresa {faturamento}, custo: {custo} lucro: {lucro} margem: {margem_lucro:.0%}")
