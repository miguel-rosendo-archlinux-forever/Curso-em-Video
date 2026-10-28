from time import sleep
def contador(i, f, p):
    print(f'contando de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(cont)
            sleep(0.5)
            cont += p
        print('FIM')
    elif i > f:
        cont = i
        while cont >= f:
            print(cont)
            sleep(0.5)
            cont -= p


contador(1, 10, 1)
contador(10, 0, 2)
print('agora é sua vez!')
ini = float(input('início: '))
fim = float(input('fim: '))
pas = abs(float(input('passo: ')))

print(f'contando de {ini} até {fim} de {pas} em {pas}')
contador(ini, fim, pas)