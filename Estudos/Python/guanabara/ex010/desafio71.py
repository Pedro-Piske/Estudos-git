'''num = int(input('Digite o valor para sacar: '))
c50 = c20 = c10 = c1 = 0
while num != 1:
    c50 = num//50
    if num < 50:
        c20 = num//20
        if num < 20:
            c10 = num //10
print(c50)
print(c20)
print(c10)# nada funciona nessa merda odeio a existencia'''

# A PARTIR DAQUI NÃO HAVERÁ MAIS CORREÇÕES, APENAS OLHAR 1 VEZ E TENTAR DE NOVO ATÉ CONSEGUIR

'''valor = int(input('Qual valor sacar: '))
total = valor
cedula = 50
cont = 0
while True:
    
    if total >= cedula:
        total = total - cedula
        cont +=1
    if total == 0:
        break
print(f'total de cedulas de 50 foi {cont}')
print(f'O total de cedulas de 20 foi {cont}')'''

#Tentativa 2:
valor = int(input('Valor a sacar: R$'))
total = valor
cedula = 50
cont = 0
while True:
    if total >= cedula:
        total = total - cedula
        cont +=1
    else:
        if cont > 0:
            print(f'O total a ser sacado foi de {cont} cedulas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont = 0   
        if total == 0:
            break           #AGORA FOI, MAS eu olhei o IF cont > 0 me dou um 6/10
   

