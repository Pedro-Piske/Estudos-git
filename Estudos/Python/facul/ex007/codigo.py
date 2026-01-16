#conjunto zé
meu_conjunto = set()
meu_conjunto.add(32)
meu_conjunto.add(55)
meu_conjunto.add(12)
print("conjunto após adicionar elementos:", meu_conjunto)

elemento = 6503024
if elemento in meu_conjunto:
    print(f"{elemento} está no conjunto")
else:
    print(f"{elemento} não tem né zé")

meu_conjunto.remove(55)
print("conjunto após remover o elemento 55:", meu_conjunto)