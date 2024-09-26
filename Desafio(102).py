def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opicional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    print('-'*20)
    for v in range(n, 0, -1):
        f *= v
        if show:
            print(v, end='')
            if v > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f

print(fatorial(5, show=True))
help(fatorial)



