l = []
p1 = 'S'
while p1 in 'Ss':
    num = int(input('digite um número: '))
    p1 = str(input('deseja continuar? [S/N] ')).strip().upper()
    l.append(num)
    if p1 == 'N':
        break
print(f'''Você digitou {len(l)} números
a média deles foi {sum(l) / len(l)} o maior foi {max(l)} o menor foi {min(l)} e a soma deles foi {sum(l)} ''')