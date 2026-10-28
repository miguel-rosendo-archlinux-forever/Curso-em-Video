
n1 = int(input('primeiro número: '))
n2 = int(input('segundo número: '))
if n1 > n2:
    print('o PRIMEIRO valor é maior')
elif n2 > n1:
    print('o SEGUNDO valor é maior')
else:
    print('os dois valores são IGUAIS')



num = int(input('digite um número inteiro:'))
print('''escolha uma das bases para a conversão: 
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('sua opção: '))
if opção == 1:
    print(f"{num} convertido para binário é {bin(num)}")



casa = float(input('valor da casa: R$'))
saláraio = float(input('salário do comprador: R$ '))
anos = int(input('quantos anos de financiamento '))
valor = float(casa / (anos * 12))
mínimo = saláraio * 30 / 100
print(f"para pagar uma casa de {casa} em {anos} anos a prestação sera de {valor:.2f}")
if valor >= mínimo:
    print('EMPRÉSTIMO NEGADO')
else:
    print('EMPRÉSTIMO ACEITO')
    
