verde = ' '
amarelo = ' '
vermelho = ' '
azul = ' '
cor = str(input('qual a cor do semaforo? '))
cor = cor.lower()
if cor == vermelho:
    print('PARE! o sinal esta fechado, espere ele ficar verde!')
elif cor == amarelo:
    print('dirija com cuidado pois o semaforo esta amarelo!')
elif cor == verde:
    print('siga em frente pois o sinal esta verde!')
elif cor == azul:
    print('siga em frente pois o sinal está azul!')
else:
    print('COR INVALIDA! digite outra vez.')