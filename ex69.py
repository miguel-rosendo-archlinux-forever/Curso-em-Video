tot18 = totH = totM20 = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('digite seu sexo[M/F] ')).strip().upper()
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'o total de pessoas com mais de 18 anos é {tot18}')
print(f'ao todo temos {totH} homens cadastrados')
print(f'e temos {totM20} mulheres com menos de 20 anos')
