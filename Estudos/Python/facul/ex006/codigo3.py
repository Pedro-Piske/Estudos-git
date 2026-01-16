preço_do_pelo_do_cu = [100,55,420,120]
imposto = 6.7
preço_final = list(map(lambda x:x * imposto,preço_do_pelo_do_cu))
print(preço_final)

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_par = list(filter(lambda x:x % 2 ==0, numeros,))
print(numeros_par)