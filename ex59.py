n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa ''')
    opcao = int(input('qual sua opcao? '))
    saborn3 = n1 + n2
    if opcao == 1:
        print(f'a soma de {n1} e {n2} e {saborn3}')
    elif opcao == 2:
        print(f'o resultado de {n1} X {n2} e {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'o maior numero entre {n1} e {n2} e {n1}')
        elif n1 < n2:
            print(f'o maior numero entre {n1} e {n2} e {n2}')
        else:
            print(f'os 2 valores digitados sao iguais')
    elif opcao == 4:
        print('informe os numeros novamente:')
        n1 = int(input('digite o primeiro valor: '))
        n2 = int(input('digite o segundo valor: '))
    elif opcao == 5:
        print('finalizando...')
    else:
        print('opcao invalida, tente novamente')
print('fim do progama, volte sempre!')