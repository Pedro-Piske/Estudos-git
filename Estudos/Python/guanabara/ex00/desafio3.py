#o primeiro codigo nao funciona pois, precisa ser considerado um numero pelo python
primeiro_numero = input()
segundo_numero = input()
soma = primeiro_numero + segundo_numero
print("soma desses numeros é",soma)

#maneira correta, utiliza-se o comando int
primeiro_numero2 = int(input())
segundo_numero2 = int(input())
soma2 = primeiro_numero2 + segundo_numero2
print("soma desses numeros é",soma2)

#maneira mais bonita
print("vamos somar dois valores")
n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))
s = n1 + n2
#print(f"a soma de {n1} + {n2} é", s) podemos usar essas duas formas
print("a soma de {} + {} é {}".format(n1, n2, s))
