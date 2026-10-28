import moeda
preço = int(input('digite o preço: R$'))
print(f'a metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'o dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'aumentando 10% de {moeda.moeda(preço)} temos {moeda.aumentar(preço, 10, True)} ')
print(f'diminuindo 23% de R${moeda.moeda(preço)} temos {moeda.diminuir(preço, 23, True)}')