num = [[], []]
for c in range (1, 8):
    valores = int(input(f'digite o {c}º valor: '))
    print('-=' * 30)
    if valores % 2 == 0:
        num[0].append(valores)
    else:
        num[1].append(valores)
num[0].sort()
num[1].sort()
print(f'os valores pares são: {num[0]}')
print(f'os valores ímpares são {num[1]}')