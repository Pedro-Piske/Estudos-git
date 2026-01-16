filmes = ["filme 1", "filme 2", "filme 3", "filme 4", "filme 5"]

print("classifique esses filmes")
print("de uma nota de 1 a 5")
print("caso não queira classificar, digite '0'.\n")

for filme in filmes:
    classificação = input(f"como classificaria esse '{filme}' de 1 a 5? (ou 0 para sair):  ")


    if classificação == '0':
     print("Que pena, você não irá mais classificar filmes hoje.")
     break


    classificação = int(classificação)
    if classificação < 1 or classificação > 5:
      print("use uma nota valida")
    else:
        print(f"vc classificou '{filme}' com {classificação} estrelas.\n")
       