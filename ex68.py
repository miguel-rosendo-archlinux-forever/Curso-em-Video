from random import randint
v = 0
while True:
    jogador = int(input('diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'você jogou {jogador} e o computador jogou {computador} o total deu {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('você VENCEU')
            v += 1
        else:
            print('você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('você VENCEU!')
            v += 1
        else:
            print('você PERDEU!')
            break
    print('vamos jogar novamente...')
print(f'GAME OVER, você venceu {v} vezes.')

    