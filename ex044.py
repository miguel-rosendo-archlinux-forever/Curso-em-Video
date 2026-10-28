from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('-==' * 20)
print("""vamos jogar pedra papel ou tesoura!""")
print('-==' * 20)
print('''
[ 1 ] pedra
[ 2 ] papel
[ 3 ] tesoura''')
jogador = input('qual a sua jogada? ')
print('-==' * 20)
print(f'computador jogou {itens[jogador]}')
print(f'jogador jogou {itens[jogador]}')
print('-==' * 20)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
        if jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
        else:
            print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
