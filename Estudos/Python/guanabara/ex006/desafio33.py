num1 = int(input("digite um numero "))
num2 = int(input("digite outro numero "))
num3 = int(input("digiteu um ultimo numero "))
if num1 > num2 & num3:
    print(f"numero {num1} é o maior")
elif num2 > num1 & num3:
    print(f"numero {num2} é o maior")
elif num3 > num1 & num2:
    print(f"numero {num3} é o maior")

if num1 < num2 % num3:
    print(f'meno nimero é {num1}')
elif num2 < num1 % num3:
    print(f"meno numero é {num2}")
elif num3 < num1 % num2:
    print(f'menor numero é {num3}')

    #por algum motivo assim nao funciona

    
#nao existe jeito facil
# correção do brabo

a = int(input("primeiro valor: "))
b = int(input("segundo valor: "))
c = int(input("Trcerio valor: "))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'o menor valor é {menor}')
print(f'o maior valor é {maior}')
