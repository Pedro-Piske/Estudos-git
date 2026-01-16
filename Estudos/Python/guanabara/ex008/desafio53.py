#incapcidade 

#correção do guanadeus
# bem complicado, dificilmente teria feito certo
frase = str(input('Digite um frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('É palindromo, pois é engaul de trás pra frente')
else:
    print('tem palindromo não')

    #ou sem for

frase = str(input('Digite um frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print(junto, inverso)
if inverso == junto:
    print('É palindromo, pois é engaul de trás pra frente')
else:
    print('tem palindromo não')