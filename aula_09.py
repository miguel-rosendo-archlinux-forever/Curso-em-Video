salário = float(input('qual o seu salário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print(f'quem ganhava R${salário}, vai passar a ganhar R${novo}')



a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c


maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'o menor número é {menor}')
print(f'e o maior é {maior}')



distância = float(input('qual é a distância da sua viagem em km?'))
valor =(distância * 0.50)
valor2 =(distância * 0.45)
print('-=-' * 11)
if distância > 200:
    print(f"o valor da viagem foi de R${valor2}")
else:
    print(f"o valor da viagem foi de R${valor}")
print('-=-' * 11)
print("tenha uma ótima viagem!")
print('-=-' * 11)



número = float(input("digite um número qualquer: "))
resultado = número % 2
if resultado == 0:
    print(f"o número {número} é par")
else:
    print(f"o número {número} é ímpar")



velocidade = int(input('qual é a velocidade atual do carro? '))
con =((velocidade - 80) * 7)
if velocidade > 80:
    print(f"você foi multado por excesso de velocidade! o valor da multa será {con}!")
print('tenha um bom dia! dirija com segurança!')



from random import randint
computador = randint(0,5)
print('-==' * 20)
print("""vou pensar em um número entre 0 e 5
tente adivinhar!""")
print('-==' * 20)
jogador = int(input('em qual número eu pensei?'))
if jogador == computador:
    print('PARABÉNS, você me venceu!')
else:
    print(f"eu venci seu otário, kkkkkkkkkkkk eu pensei no número {computador} e não no {jogador}")



n = str(input("digite uma frase:")).strip().lower()
print("analisando a frase...")
counta =(n.count('a'))
ft = (n.find('a')+1)
print(f"a letra A apareceu {counta} vezes")
print(f"a letra A apareceu na posição {ft} pela primeira vez")



nome = str(input("digite seu nome completo: ")).strip()
print ("analisando seu nome...")
print(f"seu nome em maiúsculas é {nome.upper()}")
print(f"seu nome em minúsculas é {nome.lower()}")
print(f"seu nome tem ao todo {len(nome) - nome.count(" ")} letras sem considerar espaços")
print(f"seu primeiro nome tem  {nome.find(" ")} letras")

num = int(input("informe um número: "))
n = str(num)
print(f"analizando o numero {num}...")
print(f"a unidade é {n[5]}")
print(f"a dezena é {n[4]}")
print(f"a centena é {n[3]}")
print(f"a unidade de milhar é {n[2]}")
print(f"a dezena de milhar é {n[1]}")
print(f"a centena de milhar é{n[0]}")

