def fatorial(n, show=True):
    """
        -> Fatorial de um número
    :param n: Número indicado.
    :param show: (Opcional) Mostrar ou não os cálculos.
    :return: Fatorial de um número n.
    Código por Arthur Santos
    """
    fac = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
        fac *= c
    return fac


n = int(input('Número: '))
r = input('Quer cálculos[S/N]? ').upper()
if r in 'Ss':
    show = True
    print('RESOLUÇÃO:')
else:
    show = False
print(fatorial(n, show=show))
help(fatorial)
