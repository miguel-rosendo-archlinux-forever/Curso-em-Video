print('-=' * 66)
time = ('Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Chapecoense', 'Clube do Remo', 
        'Corinthians', 'Coritiba', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Grêmio', 'Internacional', 
        'Mirassol', 'Palmeiras', 'Red Bull Bragantino', 'Santos', 'São Paulo', 'Vasco da Gama', 'Vitória')
print(f'os times do brasilerão são: {time}')
print('-=' * 66)
print(f'os 5 primeiro são {time[0:5]}')
print('-=' * 66)
print(f'os 4 últimos são {time[-5:]}')
print('-=' * 66)
print(f'times em ordem afabéticas: {sorted(time)}')
print(f'o chapecoense esta na {time.index("Chapecoense") + 1}ª posição')

