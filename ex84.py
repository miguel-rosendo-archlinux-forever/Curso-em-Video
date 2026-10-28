dados = []
listagem = []
while  True:
    dados.append(str(input('nome: ')))
    dados.append(float(input('peso: ')))
    resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    totpes += 1
    totmaior = max(dados)
    totmenor = min()
    if resp in 'N':
        break
print(f'ao todo você cadastrou {totpes} pessoas.')
print(f'o maior peso foi de {totmaior}kg peso de')
print(f'o menor peso foi de {totmenor}kg peso de')