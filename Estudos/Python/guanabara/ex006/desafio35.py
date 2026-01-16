#triangulo doido zé
r1 = int(input("Digite o valor da primeira reta do triangulo "))
r2 = int(input("Digite o valor da segunda reta do triangulo "))
r3 = int(input("Digite o valor da terceira reta do triangulo "))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print("é possivel um triangulo com essas retas")
else:
    print("tem triangulo noa zé")

# ta errado

###corrigo, nao usar or, usar and seu idiota###