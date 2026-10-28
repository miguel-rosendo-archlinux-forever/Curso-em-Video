while True:
    nome = str(input('nome: '))
    not1 = float(input('nota 1: '))
    not2 = float(input('nota 2: '))
    média = (not1 + not2) / 2
    resp = str(input('quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('-=' * 20)
print('No. NOME        MÉDIA')
print('-' * 35)
print(f'')