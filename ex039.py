from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
numsei = idade - 18
numsei02 = 18 - idade
if idade > 18:
    print(f'você ja deveria ter se alistado há {numsei} anos')
elif idade < 18:
    print(f'ainda faltam {numsei02} anos para vc se alistar')
elif idade == 18:
    print('você tem que se alistar IMEDIATAMENTE!!!!!!')