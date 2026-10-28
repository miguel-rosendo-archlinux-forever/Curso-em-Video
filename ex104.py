def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO')
        if ok:
            return valor
n = leiaint('digite um número: ')
print(f'você acabou de digitar o número {n}')