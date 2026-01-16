#listas sao mutaveis, tuplas sao imutaveis

#usar .append para adicionar elemento a lista

#USAR .insert pra adicionar elemento em uma posição especifica

#Usar del, .remove ou .pop pra eliminar um elemento
# 
# .pop normalmente é usado pra eliminar o ultimo elemento

num = [2, 5, 9, 1] 
num[2] = 3
num.append(7)
num.sort()
print(num)
num.sort(reverse=True) #Deixa do maior pro menor
num.insert(3, 120)
if 5 in num:
    num.remove(5)
else:
    print('Não tem número 5')
print(num)
print(f'Nessa lista temo {len(num)} elementos')