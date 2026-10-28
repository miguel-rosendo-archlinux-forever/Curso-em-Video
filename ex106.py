# Criando as funções de cores
def verde(texto):
    return f"\033[32m{texto}\033[m"

def vermelho(texto):
    return f"\033[31m{texto}\033[m"

def amarelo(texto):
    return f"\033[33m{texto}\033[m"

def azul(texto):
    return f"\033[34m{texto}\033[m"

def negrito(texto):
    return f"\033[1m{texto}\033[m"
from time import sleep
while True:
    print(negrito('~' * 31))
    print(negrito(verde('    SISTEMA DE AJUDA PyHelp')))
    print(negrito('~' * 31))
    comando = str(input(negrito('função ou biblioteca >>> ')))
    if comando == 'fim':
        break
    help(comando)