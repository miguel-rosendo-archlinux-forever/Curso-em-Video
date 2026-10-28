def aumentar(preço, taxa, formato=False):
    res = preço + (preço * taxa / 100)
    return res if format is False else moeda(preço)

def diminuir(preço, taxa, formato=False):
    res = preço - (preço * taxa / 100)
    return res if format is False else moeda(preço)

def dobro(preço, formato=False):
    res = preço * 2
    return res if format is False else moeda(preço)

def metade(preço, formato=False):
    res = preço / 2
    return res if format is False else moeda(preço)
    
def moeda(preço=0, moeda='R$', formato=False):
    return f'{moeda}{preço}'.replace('.', ',')