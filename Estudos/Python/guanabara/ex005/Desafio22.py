Nome = str(input("Nome completo: ")).strip()
print(f"Em maiusculo {Nome.upper()}")
print(f"Em MINUSCULO {Nome.lower()}")

print(f"Total de caractere {len(Nome)- Nome.count(" ")}")

print(f"primeiro nome {Nome.find(' ')}")
#ou
separa = Nome.split()
print(f"primeiro nome é {separa[0]}, e ele tem {len(separa[0])} letras")