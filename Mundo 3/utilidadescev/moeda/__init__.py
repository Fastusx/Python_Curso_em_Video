def metade(n=0, form=False):
    r = n / 2
    return r if form is False else moeda(r)


def dobro(n=0, form=False):
    r = n * 2
    return r if form is False else moeda(r)


def aumento(n=0, mais=0, form=False):
    r = n + (n * mais / 100)
    return r if form is False else moeda(r)


def diminuir(n=0, menos=0, form=False):
    r = n - (n * menos / 100)
    return r if form is False else moeda(r)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, mais=0, menos=0):
    print('-' * 30)
    print('       RESUMO DO VALOR')
    print('-' * 30)
    print(f'{"Preço analizado":<20}{moeda(n)}')
    print(f'{"Dobro do preço":<20}{moeda(dobro(n))}')
    print(f'{"Metade do preço":<20}{moeda(metade(n))}')
    print(f'{f"Aumento de {mais:.0f}%":<20}{moeda(aumento(n, mais))}')
    print(f'{f"Diminuição de {menos:.0f}%":<20}{moeda(diminuir(n, menos))}')
    print('-' * 30)
