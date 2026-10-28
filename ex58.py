from random import randint
computador = randint(0, 10)
palpites = 0
print('''sou seu computador...
acabei de pensar em um numero entre 0 e 10.
sera que voce consegue adivinhar qual foi?''')
jogador = int(input('qual seu palpite? '))
palpites = palpites + 1
while jogador < computador:
    jogador = int(input('mais... tente outra vez '))
    palpites = palpites + 1
while jogador > computador:
    jogador = int(input('menos... tente outra vez '))
    palpites = palpites + 1



if jogador == computador:
    print(f'voce acertou com {palpites} tentativas') 
    