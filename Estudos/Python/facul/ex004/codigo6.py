nome = input("seja bem vinda ao calculador empreserial cibertech, digite seu nome para iniciarmos: ")
email = input("Agrora por gentileza digite seu email: ")
print("Bem vinda, {nome}, portadora do email{email}")
print("vamos primeiro somar seu lucro")

faturamento = int(input("digite seu faturamento:"))
custo = int(input("agora digite seus custos"))
lucro = faturamento - custo
print("o seu lucro é de {lucro}")
print("agora vamos somar o seu imposto baseado no seu lucro a uma taxa de 10%")
imposto = lucro * 0.1
print("seu imposto é: {imposto}")
print(f"muito obrigada {nome}por usar o calculadora empreserial cibertech")
