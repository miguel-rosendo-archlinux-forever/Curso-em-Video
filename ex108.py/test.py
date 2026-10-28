import moeda
preço = int(input('digite o preço: R$'))
print(f'a metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'o dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'aumentando 10% de {moeda.moeda(preço)} temos {moeda.moeda(moeda.aumentar(preço, 10))} ')
print(f'diminuindo 23% de R${moeda.moeda(preço)} temos {moeda.moeda(moeda.diminuir(preço, 23))}')