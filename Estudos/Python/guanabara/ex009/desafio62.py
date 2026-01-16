'''p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
contagem = 1
termo = p
while contagem <= 10:
    print(f'{termo} > ', end='')
    termo = termo + r
    contagem = contagem + 1
    if contagem == 10:
        pergunta = str(input('deseja continuar? ')).upper()
        if pergunta  == 'SIM':
             r = int(input('Quantos temos que mostrar a mais? '))
        else:
            print('FIM')'''

            #tentei fazer sozinho com base na correção do 61, mas nao sou capaz

            #GRAÇAS AOS DEUSES, GUANABARA EXISTE

            #CORREÇÃO

primerio = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primerio
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} > ', end='')
        termo += razão
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos vc quer mostrar a mais? '))
print(f'cabo, foi mostrado {total} números no total')

#mais dificil do que eu esperava