
#dracula mudou todas as cores
#usar \033[m pra colocar cores no terminal, o back (40+) ta bugado por causa do dracula, use apenas o text
nome = 'Pedrada'
print(f'salve \033[1;35;40m{nome} \003[m') 
cores = {'limpa':'\033[m', 'azul':'\003[34m', 'verde': '\033[32m', 'vermelho':'\033[31m'}
#print(f'{nome(cores = 'vermelho')}''\033[m') 
#print('salve cria {}'.format(cores =['vermelho'], nome))
print("\033[7;30m salve mano")

#\033[style:0 1 4 7; text:30 ao 37; back: 40 47;m
