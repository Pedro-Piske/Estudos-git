times = ('BOTAFOGO', 'PALMEIRAS', 'FLAMENGO', 'FORTALEZA', 'INTERNACIONAL', 'SÃO PAULO', 'CORINTHIAS', 'BAHIA','CRUZEIRO', 'VASCO', 'VITÓRIA','ATLÉTICO-MG' 'FLUMINENSE', 'GRÊMIO', 'JUVENTUDE', 'RED BULL BRAGANTINO', 'ATHLETICO-PR', 'CRICIÚMA', 'ATLÉTICO-GO', 'CUIABÁ')

print(f'Os cincos primeiros colocados são{times[:5]}')
print(f'Os ultimos 4 colocados são {times[-4:]}')
print(f'Em ordem alfabetica {sorted(times)}')

if 'VITÓRIA' in times:
    print(f'O time VITÓRIA está na posição {times.index('VITÓRIA')+1}')
else:
    print('VITÓRIA não está entre os 20 primeiros colocados')
print(len(times))

#CORREÇÃO 