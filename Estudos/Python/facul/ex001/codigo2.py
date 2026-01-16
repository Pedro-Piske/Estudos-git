faturamento = 1000
custo = 700
novas_vendas = 100
faturamento = faturamento + novas_vendas
imposto = faturamento * 0.2
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento 

print("faturamento foi de", faturamento)
print("custo foi de", custo)
print("lucro foi de", lucro)
print("a margem de lucro foi", round(margem_lucro, 2))


print(10 % 3) # usa o % pra saber o resto da divisão
tempo_contrato = 170
tempo_anos = 170 / 12
tempo_meses = 170 % 12
print("tempo em anos", int(tempo_anos))
print("tempo em meses", tempo_meses)
