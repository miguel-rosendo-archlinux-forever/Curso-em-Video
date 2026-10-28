print('================== LOJAS ROSENDO ===================')
preço = int(input('preço das compras: R$'))
total1 = preço - (preço * 10 / 100)
total2 = preço - (preço * 5 / 100)
total4 = preço + (preço * 20 / 100)



print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão''')
opção = input('qual é a opção? ')
if opção == 1:
    print(f'o total da compra foi R${total1} com 10% de desconto, tenha um bom dia!')
elif opção == 2:
    print(f'o total da compra foi R${total2} com 5% de desconto, tenha um bom dia!')
elif opção == 3:
    print(f'o total da compra foi R${preço} sem juros, tenha um bom dia!')
elif opção == 4:
    totparc = int(input('quantas parcelas?'))
    parcela = total / totparc
    print(f'sua compra será parcelada em {totparc}X de R${parcela}, tenha um bom dia!')
    print(f'o total da compra foi de {total4} com juros de 20%')
