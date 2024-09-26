def metade(preço=0, formatado=False):
    res = preço / 2
    return res if formatado is False else moeda(res)
def dobro(preço=0, formatado=False):
    res = preço * 2
    return res if formatado is False else moeda(res)
def aumentar(preço=0, taxa=0, formatado=False):
    res = preço + (preço * (taxa/100))
    return res if formatado is False else moeda(res)
def reduzir(preço=0, taxa=0, formatado=False):
    res = preço - (preço * (taxa/100))
    return res if formatado is False else moeda(res)
def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
def resumo(preço=0, a=0, r=0):
    linha()
    print('RESUMO DO VALOR'.center(30))
    linha()
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{a}% de aumento: \t{aumentar(preço, a, True)}')
    print(f'{r}% de redução: \t{reduzir(preço, r, True)}')
    linha()
def linha():
    print('-' * 30)
