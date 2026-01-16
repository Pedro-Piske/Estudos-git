s1 = int(input("Salario atual: "))
p1 = s1/100*15
a1 = s1 + p1
print(f"O salario era {s1} e agora é {a1}")

#outra forma
s2 = float(input("Salario seu: "))
p2 = s2 + (s2*15/100)
print(f"Seu salario era {s2:.2f} e tu recebeu um aumento de {p2:.2f}")