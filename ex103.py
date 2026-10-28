def ficha(nome='<desconhecido>', gols=0):
    print(f'o jogador {nome} fez {gols} gol(s) no campeonato')
print('-' * 65)
nome = str(input('nome do jogador: '))
if len(nome) == 0:
    nome = '<desconhecido>'
gols = str(input('número de gols: '))
if gols == '':
    gols = 0
ficha()