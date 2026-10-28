from time import sleep
from random import randint
def sorteia(lista):
    print('sorteando 5 valores da lista')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(n)
        sleep(0.1)
    print('pronto!')
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'somando os valores pares de {lista} temos {soma}')
números = []
sorteia(números)
somapar(números)