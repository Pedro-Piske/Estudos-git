numero = int(input("digite um numero qualquer(use 0 para sair):"))
while numero != 0:
    if numero % 2 == 0:
       print("Numero par.")
    else:
        print("Numero impar")
    numero = int(input("digite outro numero(ou 0 para sair):"))
