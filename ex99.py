from time import sleep
def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('analizando os valores informados...')
    for valor in núm:
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foram informados {cont} números')
    print(f'o maior valor foi {maior}.')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()