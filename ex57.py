sexo = str(input('qual seu sexo? [M/F] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('sexo invalido, digite novamente: ')).upper().strip()[0]
print(f'sexo {sexo} registrado com sucesso.')