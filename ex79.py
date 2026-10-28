números = list()
while True:
    n = int(input('digite um valor: '))
    if n not in números:
        números.append(n)
        print('valor adicionado com sucesso...')
    else:
        print('valor duplicado, eu não adicionei esse!')
        r = str(input('quer continuar? S/N '))
        if r in 'Nn':
            break
print('-=' * 30)
números.sort()
print(f'você digitou os valores {números}')