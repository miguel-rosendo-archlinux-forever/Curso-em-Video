from random import randint
from time import sleep
print(' -' * 58)
print('JOGO DA MEGA SENA       JOGO DA MEGA SENA       JOGO DA MEGA SENA       JOGO DA MEGA SENA       JOGO DA MEGA SENA ')
print(' -' * 58)
jogos = int(input('quantos jogos serão sorteados? '))
print('- -' * 25)
print(f'- - - - - - - - - - - sorteando {jogos} jogos - - - - - - - - - - -')
for c in range(1, jogos + 1):
    pc1 = randint(1, 60)
    pc2 = randint(1, 60)
    pc3 = randint(1, 60)
    pc4 = randint(1, 60)
    pc5 = randint(1, 60)
    pc6 = randint(1, 60)
    print(f'jogo {c}: {pc1}, {pc2}, {pc3}, {pc4}, {pc5}, {pc6}')
