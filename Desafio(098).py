def contador(Início, Fim, Passo):
    print('-='*30)
    print(f'Contagem de {Início} até {Fim} de {Passo} em {Passo}')
    if Início < Fim:
        if Passo < 0:
            for n in range(Início, Fim+1, -Passo):
                print(f'{n} ', end='')
            print()
        if Passo > 0:
            for n in range(Início, Fim+1, Passo):
                print(f'{n} ', end='')
            print()
        if Passo == 0:
            for n in range(Início, Fim+1, 1):
                print(f'{n} ', end='')
            print()
    if Início > Fim:
        if Passo < 0:
            for n in range(Início, Fim-1, Passo):
                print(f'{n} ', end='')
            print()
        if Passo > 0:
            for n in range(Início, Fim-1, -Passo):
                print(f'{n} ', end='')
            print()
        if Passo == 0:
            for n in range(Início, Fim-1, -1):
                print(f'{n} ', end='')
            print()

contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início'))
f = int(input('Fim'))
p = int(input('Passo'))
contador(i, f, p)