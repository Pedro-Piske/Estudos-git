#reboot do deasfio 35
r1 = int(input("Dar o valor das reta zé: "))
r2 = int(input("Dar outro valor: "))
r3 = int(input("Ultimo valor pra ultima reta pro favor: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('dar pra fazer um triangulo com isso')
    
    if r1 == r2 == r3: 
        #todos lados iguais
        print('E por sinal é um triangulo equilátero')

    elif r1 == r2 or r1 == r3 or r2 == r3:
         # dois lados iguais
        print('Alem disso seria um triangulo isóceles')
         
    elif r1 != r2 != r3 != r1:
         #lados diferentes
        print("Contudo seria um triangulo escaleno")
else: 
    print('zero triangulos aqui')

    #ta errado
#imbecil usou or no lugar do and, agora está funcional
