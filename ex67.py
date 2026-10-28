while True:
    valor = int(input('quer ver a tabuada de qual valor? [digite um número negativo para parar] '))
    if valor < 0:
        break
    else:
        print(f'---------------------TABUADA DO {valor}-----------------------')
        for c in range(1,11):
            pro = valor * c
            print(f'{valor} X {c} = {pro}')