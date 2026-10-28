import moeda
preço = int(input('digite o preço: R$'))
print(f'a metade de R${preço} é R${moeda.metade(preço)}')
print(f'o dobro de R${preço} é R${moeda.dobro(preço)}')
print(f'aumentando 10% de R${preço} temos {moeda.aumentar(preço, 10)} ')
print(f'diminuindo 23% de R${preço} temos {moeda.diminuir(preço, 23)}')