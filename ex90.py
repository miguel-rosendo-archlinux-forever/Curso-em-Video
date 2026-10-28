nome = {}
média = {}
situação = {}
nome = str(input('nome: '))
média = float(input(f'média de {nome}: '))
print('-=' * 50)
print(f' - nome é igual a {nome}')
print(f' - média é igual a {média}')   
if média >= 7:
    print(f' - a situação de {nome} é aprovado')
elif média >= 5:
    print(f' - a situação de {nome} é recuperação')
elif média >= 0:
    print(f' - a situação de {nome} é reprovado')

'''if média >= 7:
    situação = aprovado
elif média <= 5: 
    situação = recuperação
else:
    situação = reprovado'''