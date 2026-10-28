nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
média = (nota1 + nota2) / 2
print(f'tirando {nota1} e {nota2} a média do aluno é {média}')
if média < 5:
    print('o aluno foi REPROVADO!!!')
elif média >=5 and média <= 7:
    print('o aluno está de RECUPERAÇÃO!!!')
elif média > 7:
    print('o aluno foi APROVADO!!!')
else:
    print('nota inválida')