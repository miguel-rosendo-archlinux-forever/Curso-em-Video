valores = []
while True:
    valores.append(int(input('digite um valor: ')))
    resp = str(input('quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'você digitou {len(valores)} elementos')
valores.sort(reverse = True)
print(f'os valores em ordem decrescente são: {valores}')
if 5 not in valores:
    print(f'o valor 5 não foi encontrado na lista!')
else:
    print(f'o valor 5 foi encontrado!')
