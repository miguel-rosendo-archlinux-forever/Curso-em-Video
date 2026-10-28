a = b = 0
barato = ' '
while True:
    produto = str(input('nome do produto: '))
    preço = float(input('preço: R$'))
    cont =+ 1
    a += preço
    if preço > 1000:
        b += 1
    if cont == 1:
        c = produto
    elif cont > 1:

     
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print('fim do programa')
print(f'''o total gasto foi de {a}
{b} produtos custam mais de R$1000
o produto mais barato é o {c} ''')
    
           