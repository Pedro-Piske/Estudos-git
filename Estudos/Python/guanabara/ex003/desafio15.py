a = int(input("Quantos dias o carro ficou alugado? "))
km = float(input("quantos kilometros andou? "))
ac = a * 60
kmc = km * 0.15
print(f"vc pagará {ac} pelo alguel do carro e {kmc} pelos kilometros rodados, totalizando {ac + kmc} reais")