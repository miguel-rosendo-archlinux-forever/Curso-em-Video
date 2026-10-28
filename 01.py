pr0 = int(input('qual é o salario antigo do funcionario?'))

prm6 = (pr0 / 100)
pgm5 = (prm6 * 15)
pgm8 = (pr0 + pgm5)
print(f'o salario novo do funcionario é{pgm8}')









pr1 = int(input('quanto custa o produto?'))
pr6 = (pr1 / 100)
pg7 = (pr6 * 5)
pg8 = (pr1 - pg7)
print(f'o preço do produto com desconto é {pg8}')













real = int(input('qual o seu dinheiro em reais?'))
dólar = (real * 3.27)
print(f'voçê tem {dólar} dólares, estou certo?')


mk1 = int(input('número:'))
k1 = (mk1 * 1)
k2 = (mk1 * 2)
k3 = (mk1 * 3)
k4 = (mk1 * 4)
k5 = (mk1 * 5)
k6 = (mk1 * 6)
k7 = (mk1 * 7)
k8 = (mk1 * 8)
k9 = (mk1 * 9)
k10 =(mk1 * 10)

print(f'{k1} - {k2} - {k3} - {k4} - {k5} - {k6}  - {k7} - {k8} - {k9} - {k10}')


me1 = int(input('metros'))
ce2 = (me1 * 100 )
mi3 = (me1 * 1000)

print(f'em centímetros: {ce2}')
print(f'em milimetros: {mi3}')


nota1 = int(input('nota primeira prova'))
nota2 = int(input('nota segunda prova'))
média = (nota1 + nota2) /2

print(f'média:{média}')






op = int(input('número:'))

d = op * 2
t = op * 3
rq = op ** (1/2)

print(f'o dobro de {op} é {d},  o triplo é {t} e a raiz quadrada é {rq}')

n0 = int(input('número:'))
s = n0 + 1
a = n0 - 1
print(f'o antecessor de {n0} é {a} e o sucessor é {s}')


dia = input('dia-')
mes = input('mes-')
ano = input('ano-')

print(f'voce naceu no dia {dia} de {mes} de {ano}, correto?')

n1 = int(input('primeiro numero:'))
n2 = int(input('segundo numero:'))
print(f'a soma entre {n1} e {n2} é {n1 + n2}')

n3  = int(input('primeiro número:'))
n4 = int(input('segundo número:'))
print(f'a multiplicação entre {n3} e {n4} é {n3 * n4}')

n5  = int(input('primeiro número:'))
n6 = int(input('segundo número:'))
print(f'a subtração entre {n5} e {n6} é {n5 - n6}')

n7  = int(input('primeiro número:'))
n8 = int(input('segundo número:'))
print(f'a divisão entre {n7} e {n8} é {n7 / n8}')

n10  = int(input('primeiro número:'))
n11 = int(input('segundo número:'))
print(f'{n10} elevado a {n11} é {n10 ** n11}')

n12  = int(input('primeiro número:'))
n13 = int(input('segundo número:'))
print(f'a divisão sem vírgula de {n12} e {n13} é {n12 // n13}')

n14  = int(input('primeiro número:'))
n15 = int(input('segundo número:'))
print(f'o resto da divisão {n14} e {n15} é {n14 % n15}')

n16 = int(input('número:'))
print(f'a raiz quadrada de {n16} é {n16 ** (1/2)}')

n17  = int(input('número:'))
print(f'a raiz cúbica de {n17} é {n17**(1/3)}')

a = input('digite algo: ')
print(f'é um digito? {a.isdigit()}')
print(f'é decimal? {a.isdecimal()}')
print(f'{a.isascii()}')
print(f'é alfabético? {a.isalpha()}')
print(f'é alfanumérico? {a.isalnum()}')
print(f'{a.isidentifier()}')
print(f'só tem letras minusculas? {a.islower()}')
print(f'é numerico? {a.isnumeric()}')
print(f'{a.isprintable()}')
print(f'só tem espaços? {a.isspace()}')
print(f'{a.istitle()}')
print(f'só tem letras maiusculas? {a.isupper()}')



nome = input('qual o seu nome?')
print(f'ola {nome}! seja bem vindo!')
