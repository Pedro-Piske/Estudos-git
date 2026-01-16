produto = int(input('Qual valor do produto que deseja comprar? '))
pagar = int(input('Escolha 1 pra pagar com dinheiro, e 2 se for pagar com cartão '))
dinheiro1 = produto - (produto /100 * 10)
cartão2 = produto/100*5
parcelado2 = produto
parcelado3 = produto + (produto/100*20)
if pagar == 1:
    print(f'Você escolheu pagar no dinheiro, logo o preço final será de {dinheiro1}')   
elif pagar == 2:
    pergunta1 = input('Você vai pagar no cartão, mas deseja parcelar? ')
    if pergunta1 == 'sim':
        pergunta2 = int(input('Em quantas vezes? '))
        if pergunta2 == 2:
            print(f'Nesse caso o valor do produto será {parcelado2}')
        elif pergunta2 >= 3:
            print(f'Nesse caso o valor do produto será de {parcelado3}')          
    elif pergunta1 == 'nao':
        print(f'Que bom, o valor do produto será {cartão2}')

    #### OU ####

p = float(input('Valor do produto que deseja comprar: '))
f =int(input('Escolha forma de pagamento \n [1] no dinheiro a vista\n [2] no cartao a vista\n [3] em 2x no cartao \n [4] em 3x ou mais no cartão\n '))

if f == 1:
    dindin = p - (p/100*10)
    print(f'Vai ser em dinheiro né? nesse caso o valor do produto é {dindin}')
elif f == 2:
    cartão_a_vista = p - (p/100*5)
    print(f'No cartão a vista né? Nesse caso o valor a pagar será de {cartão_a_vista}')
elif f == 3:
    print(f'Em 2 vezes no cartão, correto? Nesse caso o valor do produto é {p}')
elif f == 4:
    pergunta = input('Certo, em quantas vezes? ')
    cartão_Parcelado = p + (p/100*20)
    print(f'{pergunta} correot? nesse caso o valor será de {cartão_Parcelado}')
else:
    print('\033[0;31m OPÇÃO INVALIDA, DIGITE UMA OPÇÃO CORRETA')
 





