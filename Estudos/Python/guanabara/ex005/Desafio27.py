nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print(f'Primeiro nome é {n[0]}')
print(f'Ultimo nome é {n[len(n)-1]}')