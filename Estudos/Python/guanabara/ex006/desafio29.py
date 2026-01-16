v = int(input("Qual a velocdiade do carro: "))
#nao cosnigo resovler
if v > 80:
    print("multa nesse vagabundo")
    print(f"vai pagar 7 conto por km acima, ele estavá há {v}, logo vai tomar {v} reias de multa")
else:
    print("tá no limite, sem multa por hoje")


#     CORREÇÃO    #
Velocidade = float(input("Qual velocdiae do carro? "))
if Velocidade> 80:
    print("Vai tomar multa zé")
    multa = (Velocidade-80)* 7
    print(f"De poderosos {multa} conto")
else:
    print('Tenha um dia, dirija com cuidado')