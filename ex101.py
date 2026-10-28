def voto():
    from datetime import date
    atual = date.today().year
    print('-' * 65)
    nasc = int(input('em que ano você nasceu? '))
    idade = atual - nasc
    if idade < 16:
        print(f'com {idade} anos não vota!')
    elif 16 <= idade < 18 or idade > 70 :
        print(f'com {idade} o voto é opcional!')
    else:
        print(f'com {idade} o voto é obrigatorio')
voto()