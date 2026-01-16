def e_par (numero):
  if numero % 2 == 0:
    return True
  else:
    return False
numero = 1212302484884
if e_par(numero):
    print(f"{numero} é um número par.")
else:
    print(f"{numero} não é número par.")