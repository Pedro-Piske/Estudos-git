#feito parte ocm gguananbara e outta parte pedrada, uns 70% guaguaga

loop_idade = 0
idade_total = 0
maior_idade = 0
nome_velho = ''
muie_nova = 0

for p in range(1, 5):
    print(f'-------- {p}° PESSOA -------')
    nome = (input('Nome: ')).strip()
    
    idade = int(input('Idade: '))
    loop_idade =  loop_idade + 1
    idade_total = idade_total + idade
    
    sexo = str(input('Sexo [M/F]: ')).strip()
    if sexo in 'Ff' and idade < 20:
        muie_nova = muie_nova + 1
        
    #isso aqui é pro nome
    if p == 1 and sexo in 'Mm':
        maior_idade = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
   
media = idade_total / loop_idade
print(f'o homem mais velho tem {maior_idade} anos e se chama {nome_velho}')
print(f'a idade media do grupo é {media}')
print(f'No grupo há {muie_nova} mulheres com menos de 20 anos idade')
