salario = int(input("digite salario zé: "))
if salario >= 1250:
    aumento = salario/100*10
    tudo = salario + aumento
# ou novo = salario + (salario * 10 /100)
    print(f"houve um aumento de 10% no salario, antes era {salario}, agora é {tudo}")
else: 
    aumento = salario/100*15
    tudo = salario + aumento
# ou novo = salario +(salario * 15 /100)
    print(f"houveu m aumento de 15% no salario. antes era {salario}, agora é {tudo}")