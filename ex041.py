from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc

print(f'''o atleta tem {idade} anos''')
if idade <= 9:
    print('classificação: MIRIM')
elif idade <= 14:
    print('classificação: INFANTIL')
elif idade <= 19:
    print('classificação: JÚNIOR')
elif idade <= 25:
    print('classificação: SÊNIOR')
else:
    print('classificação: MASTER')