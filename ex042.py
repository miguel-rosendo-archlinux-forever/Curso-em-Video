#imc = peso / (altura * apeso
peso = float(input('qual o seu peso em kg? '))
altura = float(input('qual a sua altura? '))
imc = peso / (altura * altura)
print(f'seu imc é {imc}')