num = []
pares = []
ímpares = []
while True:
    num.append(int(input('digite um número: ')))
    resp = str(input('quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print(f'a lista completa é {num}')
print(f'a lista de pares é {pares}')
print(f'a lista de ímpares é {ímpares}')