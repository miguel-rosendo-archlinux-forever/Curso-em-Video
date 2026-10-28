def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indincando se deve ou não adicionar a situação
    :return: dicionario com varias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'MEHHH'
        else:
            r['situação'] = 'deploravel...'
    return r
resp = notas(10, 7, 6, sit=True)
print(resp)
# se quiser saber sobre a função digite: help(notas)
help(notas)