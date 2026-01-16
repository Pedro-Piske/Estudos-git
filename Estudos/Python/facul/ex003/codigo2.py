def soma(a,b):
  resultado = a + b
  return resultado
resultado_soma = soma(3,2)
print(resultado_soma)
def e_par (resultado_soma):
  if resultado_soma % 2 == 0:
    return True
  else:
    return False
numero = resultado_soma
if e_par(numero):
    print(f"{numero} é um número par.")
else:
    print(f"{numero} não é número par.")