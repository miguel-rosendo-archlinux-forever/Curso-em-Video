num = (int(input('digite um número: ')),
       int(input('digite outro número: ')),
       int(input('digite mais um número: ')),
       int(input('digite o último número: ')))
print(f'você digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
print(f'o valor 3 apareceu pela primeira vez na {num.index(3)+1}ª posição')