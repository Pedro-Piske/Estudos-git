valor_da_casa = int(input("Qual valor da casa que quer comprar? "))
salario = int(input('Qual seu salário? '))
anos = int(input('Em quantos anos voce vai pagar? '))
parcela = valor_da_casa / (anos * 12) 
aprovação = salario/100*30
if aprovação < parcela: 
    print('emprestimo negado')
else:
    print('emprestimo aprovado')